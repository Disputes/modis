def get_event_handlers():
    """Gets dictionary of event handlers and the modules that define them

    Returns:
        event_handlers (dict): Contains "all", "on_ready", "on_message", "on_reaction_add", "on_error"
    """

    import os
    import importlib

    # Define dict
    event_handlers = {
        "on_ready": [],
        "on_message": [],
        "on_reaction_add": [],
        "on_error": []
    }

    # Get list of all modules
    mlist = []
    modules_dir = os.path.dirname(os.path.realpath(__file__))
    for m in os.listdir(modules_dir):
        if os.path.isdir("{}\\{}".format(modules_dir, m)) and not m.startswith("_"):
            mlist.append(importlib.import_module("module_database.{}".format(m)))

    # For each event handler type, sweep through modules and add all defined event handlers
    for m in mlist:
        if "on_ready" in dir(m):
            event_handlers["on_ready"].append(m.on_ready)

        if "on_message" in dir(m):
            event_handlers["on_message"].append(m.on_message)

        if "on_reaction_add" in dir(m):
            event_handlers["on_reaction_add"].append(m.on_reaction_add)

        if "on_error" in dir(m):
            event_handlers["on_error"].append(m.on_error)

    return event_handlers


def get_required_perms():
    """Returns Discord API Permissions object with all the permissions the modules require

    Returns:
        perms (discord.Permissions): The permissions this bot requires
    """

    import discord

    perms = discord.Permissions()

    perms.add_reactions = True
    perms.read_messages = True
    perms.send_messages = True
    perms.send_tts_messages = True
    perms.manage_messages = True
    perms.connect = True
    perms.speak = True

    return perms