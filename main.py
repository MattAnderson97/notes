from topic import Topic


def print_topic(topic: Topic, depth=0):
    print(("    " * depth) +  f"{topic.get_name()}")
    for child in topic.get_topics():
        print_topic(child, depth+1)
    for entry in topic.get_entries():
        print(("    " * (depth + 1)) +  f"{entry}")


if __name__ == "__main__":
    parent = Topic(1, "parent topic")
    parent.add_entry("entry 1")
    parent.add_entry("entry 2")
    child = Topic(2, "sub-topic", parent)
    child.add_entry("sub-entry 1")
    child.add_entry("sub-entry 2")
    child.update_in_parent()
    child_2 = Topic(3, "sub-topic 2", parent)
    child_2.add_entry("sub-entry 3")
    child_2.add_entry("sub-entry 4")
    child_2.update_in_parent()

    print_topic(parent)