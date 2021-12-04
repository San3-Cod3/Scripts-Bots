# Scripts-Bots
Scripts and Bots

* PythonBotTest.py | This is basically a simple skeleton for now, for people to test.  I'll add more to it once I get people on board.  Python required to be installed on your system - tested with Python 3.2.3 on Windows only.  Either download it or copy entire contents to a blank file on your system with .py extension.  Only one server works at a time per instance, so, you will need to run as many instances for how many servers you want to run the bot on, and although the bot can be joined to multiple channels, the way its commands work, will not allow them to work inside other channels than the main (unless things are written differently), and any commands issued in and directly from another chanel will actually show the output return in the main channel.  So, just run multiple instances and edit the script of each instance to use the bot in multiple channels and on multiple servers/networks.
* - To start the bot, make sure Python is on your Windows system and just double click the *.py file or right click it and select 'Open' from the context menu to launch it - this will bring up a terminal console command window where you can see what's going on and it connecting etc.
* - '!spit' is a debug command used to 'spit' out how the bot sees 'you' on IRC into the channel, (can be removed when no longer needed), 'you' as in: n/Nick!~i/Ident@h/Host - you can then, if you like, define the variable: master = "nick!~ident@host" | This is especially helpful if you have a coloured or bold or both vHost as you can use what the bot spits out to make the bot recognise only you when using commands that you don't want anyone else using, such as the quit command below; which is a version geard more toward recognising the user's coloured and/or bold+coloured vHost specifically - you would replace nick!, ~ident and @host with the version the bot spits out for you, what it outputs is how it sees you, your nick, your ident and your host on IRC, example: master = "Git!~Hub@\x02\x034This\x0311Looks\x039Like\x036Coloured\x037vHost\x0314Output\x0f"
### vHost/bold+coloured vHost - master string quit section (START) ###

    Quit_Stuff = text.strip('\n\r') # Removing any unnecessary linebreaks.

    name = Quit_Stuff.split(' ',1)[0][1:] # We split out the name

    if name.lower() == master.lower() and Quit_Stuff.find(":quit " + botnick) != -1:
        quitting()
        irc.send(bytes("QUIT \n", "UTF-8"))
    else:
        if name.lower() != master.lower() and Quit_Stuff.find(":quit " + botnick) != -1:
            ircwrite("PRIVMSG "+ channel +" :You do NOT match master string! \r\n")

### vHost/bold+coloured vHost - master string quit section (END) ###


# ¦¦¦ #


### vHost/bold+coloured vHost -- master string change botnick section (START) ###

    Nick_Stuff = text.strip('\n\r') # Removing any unnecessary linebreaks.

    name2 = Nick_Stuff.split(' ',1)[0][1:] # We split out the name

    if name2.lower() == master.lower() and Nick_Stuff.find(':!nick') != -1:
        nickname = text.split(':!nick')
        if len(nickname) < 2:
            pass
        else:
            nicknames = nickname[1].strip()
            ircwrite('NICK '+ (nicknames) +'\r\n')
    else:
        if name2.lower() != master.lower() and Nick_Stuff.find(':!nick') != -1:
            ircwrite("PRIVMSG "+ channel +" :You do NOT match master string! \r\n")

### vHost/bold+coloured vHost -- master string change botnick section (END) ###
