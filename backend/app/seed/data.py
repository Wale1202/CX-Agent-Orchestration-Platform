"""Static demo data used to populate a fresh database.

These rows give the chat and dashboard something to display from the first
run, and give the ``lookup_order`` tool real records to query against.
"""

from decimal import Decimal


CUSTOMERS = [
    {"name": "Alice Johnson", "email": "alice@example.com", "tier": "pro"},
    {"name": "Bob Martinez", "email": "bob@example.com", "tier": "free"},
    {"name": "Chen Wei", "email": "chen@example.com", "tier": "enterprise"},
    {"name": "Diana Patel", "email": "diana@example.com", "tier": "free"},
]


# Orders reference customers by ``email`` so the seed script can resolve the
# foreign key after customers are inserted.
ORDERS = [
    {
        "customer_email": "alice@example.com",
        "order_reference": "ORD-1001",
        "status": "delivered",
        "total_amount": Decimal("129.99"),
    },
    {
        "customer_email": "alice@example.com",
        "order_reference": "ORD-1002",
        "status": "shipped",
        "total_amount": Decimal("42.50"),
    },
    {
        "customer_email": "bob@example.com",
        "order_reference": "ORD-1003",
        "status": "pending",
        "total_amount": Decimal("18.00"),
    },
    {
        "customer_email": "chen@example.com",
        "order_reference": "ORD-1004",
        "status": "refunded",
        "total_amount": Decimal("250.00"),
    },
    {
        "customer_email": "chen@example.com",
        "order_reference": "ORD-1005",
        "status": "cancelled",
        "total_amount": Decimal("75.25"),
    },
    {
        "customer_email": "diana@example.com",
        "order_reference": "ORD-1006",
        "status": "delivered",
        "total_amount": Decimal("9.99"),
    },
]


KNOWLEDGE_BASE_ARTICLES = [
    {
        "title": "How to track your order",
        "category": "shipping",
        "tags": ["tracking", "shipping", "delivery"],
        "content": (
            "You can track any order from your account dashboard under "
            "'Orders'. Each order has a tracking number that updates within "
            "24 hours of shipment. If your tracking number hasn't updated "
            "after 48 hours, contact support."
        ),
    },
    {
        "title": "Refund policy",
        "category": "billing",
        "tags": ["refund", "returns", "billing"],
        "content": (
            "We offer a 30-day refund window from the date of delivery. "
            "Refunds are issued to the original payment method and typically "
            "process within 5-7 business days. Items must be returned in "
            "their original condition."
        ),
    },
    {
        "title": "How to cancel an order",
        "category": "shipping",
        "tags": ["cancellation", "orders"],
        "content": (
            "You can cancel an order from your account as long as it hasn't "
            "shipped yet. Once an order's status is 'shipped' it can no "
            "longer be cancelled — you'll need to wait for delivery and "
            "request a return instead."
        ),
    },
    {
        "title": "Resetting your password",
        "category": "account",
        "tags": ["password", "login", "security"],
        "content": (
            "Click 'Forgot password' on the login page and enter your email. "
            "You'll receive a reset link valid for 1 hour. If the email "
            "doesn't arrive, check spam and confirm the email matches the "
            "one on your account."
        ),
    },
    {
        "title": "Managing your subscription",
        "category": "billing",
        "tags": ["subscription", "plans", "billing"],
        "content": (
            "Subscription changes are made from Account → Billing. Upgrades "
            "take effect immediately and are prorated. Downgrades take "
            "effect at the end of the current billing cycle."
        ),
    },
    {
        "title": "Shipping options and timelines",
        "category": "shipping",
        "tags": ["shipping", "delivery", "options"],
        "content": (
            "Standard shipping arrives in 3-5 business days. Express "
            "shipping arrives in 1-2 business days for an additional fee. "
            "International shipping varies by destination, typically 7-14 "
            "business days."
        ),
    },
    {
        "title": "Updating account email or contact info",
        "category": "account",
        "tags": ["account", "email", "contact"],
        "content": (
            "Go to Account → Settings to change your email address or phone "
            "number. Email changes require confirmation from both the old "
            "and new address for security."
        ),
    },
    {
        "title": "Troubleshooting failed payments",
        "category": "billing",
        "tags": ["payment", "billing", "troubleshooting"],
        "content": (
            "If a payment fails, check that your card hasn't expired and "
            "that billing details match your card on file. We retry failed "
            "payments automatically for 3 days before suspending an order."
        ),
    },
]
