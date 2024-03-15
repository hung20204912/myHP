# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import click

from eth_utils import keccak

from blockchainetl.file_utils import smart_open
from blockchainetl.logging_utils import logging_basic_config


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-i', '--input-string', default='Transfer(address,address,uint256)', show_default=True, type=str,
              help='String to hash, e.g. Transfer(address,address,uint256)')
@click.option('-o', '--output', default='-', show_default=True, type=str, help='The output file. If not specified stdout is used.')
def get_keccak_hash(input_string, output):
    """Outputs 32-byte Keccak hash of given string."""
    hash = keccak(text=input_string)

    with smart_open(output, 'w') as output_file:
        output_file.write('0x{}\n'.format(hash.hex()))


def get_keccak_hash_now(input_string, output):
    """Outputs 32-byte Keccak hash of given string."""
    hash = keccak(text=input_string)

    with smart_open(output, 'w') as output_file:
        output_file.write('0x{}\n'.format(hash.hex()))


# input_string = "LiquidationCall(address,address,address,uint256,uint256,address,bool)" #### -> e413a321e8681d831f4dbccbca790d2952b56f977908e45be37335533e005286
# input_string = "Transfer(address,address,uint256)"
# input_string = "initializeBondTerms(uint256,uint256,uint256,uint256,uint256,uint256,uint256)"
# input_string = "claim(address)"
# input_string = "stake(uint256,address)"
# input_string = "forfeit()"
# input_string = "unstake(uint256,bool)"
input_string = "Deposit(address,address,address,uint256,uint16)"

hash = keccak(text=input_string)
print(hash.hex())