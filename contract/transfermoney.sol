//SPDX-License-ldentifier: MIT

pragma solidity ^0.8.0;

import "hardhat/console.sol";

contract store_money {
    uint256 amount;
    address payee;
    address payer;

    constructor() {
        console.log(msg.sender);
    }

    function weixin(
        uint256 amount_to_pay,
        address payer_add,
        address payee_add
    ) public {
        amount = amount_to_pay;
        payee = payee_add;
        payer = payer_add;
    }

    function check_transaction() public view returns (
            address,
            address,
            uint256
        )
    {
        return (payee, payer, amount);
    }
}
