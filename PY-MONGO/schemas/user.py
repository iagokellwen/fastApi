def chatEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "pergunta": item["pergunta"],
        "resposta": item["resposta"],
    }


def chatsEntity(entity) -> list:
    return [chatEntity(item) for item in entity]
