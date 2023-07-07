from temple_web.myconfig import PaymentGatewayConfig
import json
import requests
from datetime import date, datetime


import logging

log = logging.getLogger(__name__)


def create_order(
    client_txn_id: str,
    redirect_url: str,
    amount: int,
    product_info: str = "",
    customer_name: str = "",
    customer_email: str = "",
    customer_mobile: str = "",
) -> dict | None:
    """Wrapper to call the create_order enpoint

    Args:
        client_txn_id (str): Unique id for this order. Needed again to check the order.
        redirect_url (str): The URL that will receive the callback/redirect
        from the payment gateway after payment is done
        amount (int): Amount in INR
        product_info (str): Product name or relevant information
        customer_name (str): Customer full name
        customer_email (str): Customer email address
        customer_mobile (str): Customer phone number


    Returns: data returned by API
        dict:
        - order_id
        - payment_url

    For all cases of failure issue will be logged, and None will be returned
    """
    if not customer_email:
        customer_email = "example@example.com"
    payload_dict = {
        "key": str(PaymentGatewayConfig.API_KEY),
        "client_txn_id": client_txn_id,
        "amount": str(amount),
        "p_info": product_info,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "customer_mobile": customer_mobile,
        "redirect_url": redirect_url,
        "udf2": f"datetime {str(datetime.now())}",
    }
    payload_dict.update(PaymentGatewayConfig.USER_DEFINED_FIELDS)

    payload_json_str = json.dumps(payload_dict)

    response = requests.request(
        "POST",
        PaymentGatewayConfig.CREATE_ORDER,
        headers=PaymentGatewayConfig.REQUEST_HEADERS,
        data=payload_json_str,
    )

    if response.status_code == 200:
        rj = response.json()
        if rj["status"] is True:
            return True, rj["data"]
        else:
            log.warning("Failed to create order \n%s", response.text)
            return False, response
    else:
        log.warning(
            "Payment Gateway create_order returned non 200 code \n %s", response.text
        )
        return False, response


def check_order_status(client_txn_id: str, txn_date: date = None):
    """Wrapper to call the check_order_status endpoint

    Args:
        client_txn_id (str): The unique id used to create the order
        txn_date (date, optional): The date when order was created,
        as python datetime.date object.
        Defaults to date.today()

    Returns:
        dict: The data returned by the api

        - id: int
        - customer_vpa
        - amount: int
        - client_txn_id,
        - customer_name
        - customer_email
        - customer_mobile
        - p_info
        - upi_txn_id
        - status
        - remark
        - "udf1":"user defined field 1",
        - "udf2":"user defined field 2",
        - "udf3":"user defined field 3",
        - redirect_url
        - txnAt
        - createdAt,
        - "Merchant":{"name":"","upi_id":""}
    """

    if txn_date is None:
        txn_date = date.today()

    fmted_txn_date = txn_date.strftime("%d-%m-%Y")

    payload = json.dumps(
        {
            "key": PaymentGatewayConfig.API_KEY,
            "client_txn_id": client_txn_id,
            "txn_date": fmted_txn_date,
        }
    )
    response = requests.request(
        "POST",
        PaymentGatewayConfig.CHECK_ORDER_STATUS,
        headers=PaymentGatewayConfig.REQUEST_HEADERS,
        data=payload,
    )

    if response.status_code == 200:
        rj = response.json()
        if rj["status"] is True:
            return rj["data"]
        else:
            log.warning("Failed to find transanction \n%s", response.text)
    else:
        log.warning(
            "Payment Gateway check_order_status returned non 200 code \n %s",
            response.text,
        )
    return None
