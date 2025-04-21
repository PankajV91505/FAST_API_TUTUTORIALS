def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "importance": item["importance"]
    }
    
def notesEntity(entity) -> list:
    return [noteEntity(item) for item in entity]
    
    

        