import Datapyck
Datapack = Datapyck.Datapack("Test Datapack", "Made by Matthew Schlauderaff using the Datapyck Python module", "1.19.3")
welcome = Datapyck.Tellraw("everyone", "The datapack has loaded!", color="green", bold=True, underline=True)
Datapack.write("load", welcome)
list1 = Datapyck.Tellraw("@a", "Press to see list of players in server: ")
list2 = Datapyck.KeybindTellraw("@a", "list", underline=True)
Datapack.write("load", Datapyck.CombineTellraw("everyone", list1, list2))