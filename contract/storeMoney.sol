// SPDX-License-Identifier: GPL-3.0

pragma solidity = 0.8;

contract Storage {

    uint num1;

    function store_m(uint num) public {
        num1 = num;
    }

    function view_m() public view returns (uint) {
        return num1 ;
    }
}
