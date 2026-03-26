def list_tickets(customer_id: str):
    """
    Toy ticket list. Replace with real data source.
    """
    return {
        "customer_id": customer_id,
        "tickets": [
            {"id": "T1", "status": "open"},
            {"id": "T2", "status": "closed"},
        ],
    }
