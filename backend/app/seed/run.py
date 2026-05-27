"""Populate the database with demo data.

Idempotent: if any customers already exist the script exits without making
changes. Run with ``python -m app.seed.run``.
"""

from sqlalchemy import select

from app.db import SessionLocal, init_db
from app.models import Customer, KnowledgeBaseArticle, Order
from app.seed.data import CUSTOMERS, KNOWLEDGE_BASE_ARTICLES, ORDERS


def seed() -> None:
    init_db()

    with SessionLocal() as db:
        existing = db.execute(select(Customer).limit(1)).scalar_one_or_none()
        if existing is not None:
            print("Database already has data — skipping seed.")
            return

        # Customers first so we can resolve their IDs for the orders.
        customers_by_email: dict[str, Customer] = {}
        for row in CUSTOMERS:
            customer = Customer(**row)
            db.add(customer)
            customers_by_email[row["email"]] = customer
        db.flush()  # populates customer.id without committing

        for row in ORDERS:
            email = row["customer_email"]
            db.add(
                Order(
                    customer_id=customers_by_email[email].id,
                    order_reference=row["order_reference"],
                    status=row["status"],
                    total_amount=row["total_amount"],
                )
            )

        for row in KNOWLEDGE_BASE_ARTICLES:
            db.add(KnowledgeBaseArticle(**row))

        db.commit()

    print(
        f"Seeded {len(CUSTOMERS)} customers, {len(ORDERS)} orders, "
        f"{len(KNOWLEDGE_BASE_ARTICLES)} knowledge base articles."
    )


if __name__ == "__main__":
    seed()
