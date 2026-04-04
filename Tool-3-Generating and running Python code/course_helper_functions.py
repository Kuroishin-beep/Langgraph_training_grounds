def pretty_print_messages(messages_or_update):
    """
    Helper function to nicely print LangChain/LangGraph messages.
    Handles both lists of messages and LangGraph node updates (dicts).
    """
    # If it's a LangGraph chunk (dict mapping node_name -> state update)
    if isinstance(messages_or_update, dict):
        # Extract the node name and the state update
        for node_name, state in messages_or_update.items():
            print(f"---\n🚀 Node execution: {node_name}\n---")
            messages = state.get("messages", [])
            if not isinstance(messages, list):
                messages = [messages]
            _print_messages_list(messages)
    # If it's a direct list of messages
    elif isinstance(messages_or_update, list):
        _print_messages_list(messages_or_update)
    else:
        print(messages_or_update)

def _print_messages_list(messages):
    for message in messages:
        # Check if the object has a type attribute before checking it
        if not hasattr(message, "type"):
            continue
            
        if message.type == "system":
            print(f"System: {message.content}\n")
        elif message.type == "human":
            print(f"Human: {message.content}\n")
        elif message.type == "ai":
            print(f"AI: {message.content}\n")
            if getattr(message, "tool_calls", None):
                for tool_call in message.tool_calls:
                    print(f"  [Tool Call]: {tool_call['name']}({tool_call['args']})\n")
        elif message.type == "tool":
            print(f"Tool Result ({message.name}):\n{message.content}\n")
        else:
            print(f"{message.type.capitalize()}: {message.content}\n")
