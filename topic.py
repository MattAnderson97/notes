from __future__ import annotations


class Topic:
    """
    create a new topic
    """
    def __init__(self, id: int, name: str, parent: Topic = None) -> None:
        self.id = id
        self._name = name
        self._entries = []
        self._topics = []
        if parent:
            self.set_parent(parent)

    def get_name(self) -> str:
        return self._name

    def add_entry(self, entry: str) -> None:
        self._entries.append(entry)

    def get_entries(self) -> list:
        return self._entries

    def add_topic(self, topic: Topic) -> None:
        self._topics.append(topic)

    def get_topics(self) -> list:
        return self._topics

    def set_parent(self, topic: Topic) -> None:
        self._parent = topic
        self._parent.add_topic(self)

    def update_child_topic(self, topic: Topic) -> None:
        _topic = next(filter(lambda t: t.id == topic.id, self._topics), False) # get topic from list if it exists, else False
        if _topic: # old version of topic
            index = self._topics.index(_topic) # index of old version
            self._topics[index] = topic # update topic in list

    def update_in_parent(self) -> None:
        self._parent.update_child_topic(self)