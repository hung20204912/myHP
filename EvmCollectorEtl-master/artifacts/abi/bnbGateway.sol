// SPDX-License-Identifier: agpl-3.0
pragma solidity 0.6.12;
pragma experimental ABIEncoderV2;

import {Ownable} from '../../dependencies/openzeppelin/contracts/Ownable.sol';
import {IBEP20} from '../../dependencies/openzeppelin/contracts/IBEP20.sol';
import {IWBNB} from '../../interfaces/IWBNB.sol';
import {IWBNBGateway} from '../../interfaces/IWBNBGateway.sol';
import {ILendingPool} from '../../interfaces/ILendingPool.sol';
import {IStakedTrava} from "../../interfaces/IStakedTrava.sol";
import {ITToken} from '../../interfaces/ITToken.sol';
import {ReserveConfiguration} from '../../protocol/libraries/configuration/ReserveConfiguration.sol';
import {UserConfiguration} from '../../protocol/libraries/configuration/UserConfiguration.sol';
import {Helpers} from '../../protocol/libraries/helpers/Helpers.sol';
import {DataTypes} from '../../protocol/libraries/types/DataTypes.sol';


contract BNBGateway is IWBNBGateway, Ownable {
  using ReserveConfiguration for DataTypes.ReserveConfigurationMap;
  using UserConfiguration for DataTypes.UserConfigurationMap;

  IWBNB internal immutable WBNB;

  /**
   * @dev Sets the WBNB address and the LendingPoolAddressesProvider address. Infinite approves lending pool.
   * @param wbnb Address of the Wrapped BNB contract
   **/
  constructor(address wbnb) public {
    WBNB = IWBNB(wbnb);
  }

  function authorizeLendingPool(address lendingPool) external onlyOwner {
    WBNB.approve(lendingPool, uint256(-1));
  }

  /**
   * @dev deposits WETH into the reserve, using native ETH. A corresponding amount of the overlying asset (aTokens)
   * is minted.
   * @param lendingPool address of the targeted underlying lending pool
   * @param onBehalfOf address of the user who will receive the aTokens representing the deposit
   * @param referralCode integrators are assigned a referral code and can potentially receive rewards.
   **/
  function depositBNB(
    address lendingPool,
    address onBehalfOf,
    uint16 referralCode
  ) external payable override{
    WBNB.deposit{value: msg.value}();
    ILendingPool(lendingPool).deposit(address(WBNB), msg.value, onBehalfOf, referralCode);
  }

  /**
   * @dev withdraws the WBNB _reserves of msg.sender.
   * @param lendingPool address of the targeted underlying lending pool
   * @param amount amount of aWBNB to withdraw and receive native BNB
   * @param to address of the user who will receive native BNB
   */
  function withdrawBNB(
    address lendingPool,
    uint256 amount,
    address to
  ) external override{  
    ITToken aWBNB = ITToken(ILendingPool(lendingPool).getReserveData(address(WBNB)).tTokenAddress);
    uint256 userBalance = aWBNB.balanceOf(msg.sender);
    uint256 amountToWithdraw = amount;

    // if amount is equal to uint(-1), the user wants to redeem everything
    if (amount == type(uint256).max) {
      amountToWithdraw = userBalance;
    }
    aWBNB.transferFrom(msg.sender, address(this), amountToWithdraw);
    ILendingPool(lendingPool).withdraw(address(WBNB), amountToWithdraw, address(this));
    WBNB.withdraw(amountToWithdraw);
    _safeTransferBNB(to, amountToWithdraw);
  }

  /**
   * @dev repays a borrow on the WBNB reserve, for the specified amount (or for the whole amount, if uint256(-1) is specified).
   * @param lendingPool address of the targeted underlying lending pool
   * @param amount the amount to repay, or uint256(-1) if the user wants to repay everything
   * @param onBehalfOf the address for which msg.sender is repaying
   */
  function repayBNB(
    address lendingPool,
    uint256 amount,
    address onBehalfOf
  ) external payable override {
    (uint256 variableDebt) =
      Helpers.getUserCurrentDebtMemory(
        onBehalfOf,
        ILendingPool(lendingPool).getReserveData(address(WBNB))
      );

    uint256 paybackAmount = variableDebt;

    if (amount < paybackAmount) {
      paybackAmount = amount;
    }
    require(msg.value >= paybackAmount, 'msg.value is less than repayment amount');
    WBNB.deposit{value: paybackAmount}();
    ILendingPool(lendingPool).repay(address(WBNB), msg.value, onBehalfOf);

    // refund remaining dust BNB
    if (msg.value > paybackAmount) _safeTransferBNB(msg.sender, msg.value - paybackAmount);
  }

  /**
   * @dev borrow WBNB, unwraps to BNB and send both the BNB and DebtTokens to msg.sender, via `approveDelegation` and onBehalf argument in `LendingPool.borrow`.
   * @param lendingPool address of the targeted underlying lending pool
   * @param amount the amount of BNB to borrow
   * @param referralCode integrators are assigned a referral code and can potentially receive rewards
   */
  function borrowBNB(
    address lendingPool,
    uint256 amount,
    uint16 referralCode
  ) external override {
    ILendingPool(lendingPool).borrow(
      address(WBNB),
      amount,
      referralCode,
      msg.sender
    );
    WBNB.withdraw(amount);
    _safeTransferBNB(msg.sender, amount);
  }

  /**
   * @dev transfer BNB to an address, revert if it fails.
   * @param to recipient of the transfer
   * @param value the amount to send
   */
  function _safeTransferBNB(address to, uint256 value) internal {
    (bool success, ) = to.call{value: value}(new bytes(0));
    require(success, 'BNB_TRANSFER_FAILED');
  }

  /**
   * @dev transfer ERC20 from the utility contract, for ERC20 recovery in case of stuck tokens due
   * direct transfers to the contract address.
   * @param token token to transfer
   * @param to recipient of the transfer
   * @param amount amount to send
   */
  function emergencyTokenTransfer(
    address token,
    address to,
    uint256 amount
  ) external onlyOwner {
    IBEP20(token).transfer(to, amount);
  }

  /**
   * @dev transfer native BNB from the utility contract, for native BNB recovery in case of stuck BNB
   * due selfdestructs or transfer BNB to pre-computated contract address before deployment.
   * @param to recipient of the transfer
   * @param amount amount to send
   */
  function emergencyBNBTransfer(address to, uint256 amount) external onlyOwner {
    _safeTransferBNB(to, amount);
  }

  /**
   * @dev Get WBNB address used by WBNBGateway
   */
  function getWBNBAddress() external view returns (address) {
    return address(WBNB);
  }

  /**
   * @dev Only WBNB contract is allowed to transfer BNB here. Prevent other addresses to send BNB to this contract.
   */
  receive() external payable {
    require(msg.sender == address(WBNB), 'Receive not allowed');
  }

  /**
   * @dev Revert fallback calls
   */
  fallback() external payable {
    revert('Fallback not allowed');
  }
} 