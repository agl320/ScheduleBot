import os
import random
import json

import discord
from discord.ext import commands

class scheduler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = json.load(open("config.json"))
        self.user_base = self.config["user_base"]

    @commands.Cog.listener()
    async def on_ready(self):
        print("scheduler loaded.")

    @commands.command(aliases = ["Notes","Note","notes","note"])
    async def note_master(self, ctx, *args):

        self.script_dir = os.path.dirname(__file__) # get current address
        self.rel_path = f"users/{str(ctx.message.author.id)}_note.txt" # new file
        self.abs_file_path = os.path.join(self.script_dir, self.rel_path) # join addresses
        print(str(self.abs_file_path))

        if str(ctx.message.author.id) not in self.user_base: # if new user

            self.user_base.append(str(ctx.message.author.id)) # update user list

            await ctx.send(f"Unrecognized; added ID: {ctx.message.author.id}")

            with open(str(self.abs_file_path),"w") as f: # create new file in path
                f.close()

            self.config["user_base"] = self.user_base # update actualy config
            with open("config.json","w") as cfg:
                cfg.write(json.dumps(self.config))

    @commands.command(aliases = ["Schedule", "schedule"])
    async def event_master(self, ctx, *args):
        print(ctx.message.author.id)
        print(self.user_base)

        self.script_dir = os.path.dirname(__file__) # get current address
        self.rel_path = f"users/{str(ctx.message.author.id)}_sch.txt" # new file
        self.abs_file_path = os.path.join(self.script_dir, self.rel_path) # join addresses
        print(str(self.abs_file_path))

        if str(ctx.message.author.id) not in self.user_base: # if new user

            self.user_base.append(str(ctx.message.author.id)) # update user list

            await ctx.send(f"Unrecognized; added ID: {ctx.message.author.id}")

            with open(str(self.abs_file_path),"w") as f: # create new file in path
                f.close()

            self.config["user_base"] = self.user_base # update actualy config
            with open("config.json","w") as cfg:
                cfg.write(json.dumps(self.config))

        if args[0] == 'add':
            print("Adding to schedule...")
            file = open(self.abs_file_path, "a+")
            file.write(f"{args[1]}\n")
            await ctx.send(f"Event: {args[1]} added!")
            file.close()
            print("Added!")

        if args[0] == 'read':
            print("Reading from schedule...")
            with open(self.abs_file_path) as file:
                if os.stat(self.abs_file_path).st_size != 0:
                    index = 1
                    for line in file:
                        await ctx.send(f"Event {index}: {line}")
                        index += 1
                else:
                    await ctx.send("No events currently!")
            file.close()
            print('Done!')

        if args[0] == 'delete':
            print("Deleting specified events...")
            if args [1] == 'all':
                open(self.abs_file_path, "w").close()
                await ctx.send("All events have been deleted :cry:")
            else:
                deleteIndex = int(args[1])
                with open(self.abs_file_path, "r") as f:
                    lines = f.readlines()
                with open(self.abs_file_path, "w") as f:
                    index = 0
                    deleted = False
                    for line in lines:
                        if index == deleteIndex:
                            await ctx.send(f"Event {line} has been deleted!")
                            deleted = True
                        else:
                            f.write(line)
                        index += 1
                    if deleted == False:
                        await ctx.send("No event at that index!")




        print("Done!")


def setup(client):
    client.add_cog(scheduler(client))
