def impact_score(category: str):
    # simple impact estimation for demo
    scores = {
        "wet": {"co2_saved": 0.2, "note": "Composting reduces methane from landfill."},
        "dry": {"co2_saved": 0.5, "note": "Recycling saves energy and raw materials."},
        "hazardous": {"co2_saved": 0.3, "note": "Prevents toxic contamination of soil/water."},
        "e-waste": {"co2_saved": 0.8, "note": "Recover metals and reduce mining demand."},
    }
    return scores.get(category, {"co2_saved": 0.1, "note": "Proper disposal supports sustainability."})