from interactions import slash_command, OptionType, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension
import os
import requests
class Charakter(Extension):
        @slash_command("character", description="This will send information about the character including a link to the wiki page")
        @slash_option(
            name="name",
            description="String Option",
            required=True,
            opt_type=OptionType.STRING
        )
        async def character(self, ctx: SlashContext, *kwargs):
                lines = [];
                response = requests.get("https://the-one-api.dev/v2/character", headers={'Accept': 'application/json','Authorization': os.getenv('LOTR_API')})
                #response.status_code response code variable
                records = response.json()
                returnText = ""

                if response.ok:
                        # Choose a random record
                        found_record = next((record for record in records.get('docs', []) if (record.get('name').lower().find(kwargs[0].lower())) != -1), None)
                        print(found_record)
                        if found_record != None:
                                 #Defining every line
                                lines.append("Name: " + found_record.get('name')) 
                                lines.append("Race: " + found_record.get('race')) 
                                if found_record.get('gender') != "": lines.append("Gender: " + found_record.get('gender')) 
                                if found_record.get('birth') != "": lines.append("Birth: " + found_record.get('birth')) 
                                if found_record.get('death') != "": lines.append("Death: " + found_record.get('death')) 
                                if found_record.get('realm') != "": lines.append("Realm: " + found_record.get('realm')) 
                                if found_record.get('hair') != "": lines.append("Hair: " + found_record.get('hair')) 
                                if found_record.get('height') != "": lines.append("Height: " + found_record.get('height')) 
                                lines.append("Wikipage: " + found_record.get('wikiUrl')) 
                                #Including all the lines in one single string
                                for line in lines:
                                        returnText = returnText + line + "\n"
                        else:
                                returnText = "I could not find such a being"
                else:
                        returnText = "Something went wrong"
                        print(response.status_code)
                
               
                #Returning said string
                await ctx.send(returnText)
        @character.error
        async def command_error(self, e, *args, **kwargs):
                print(f"Command hit error with {args=}, {kwargs=}")

        # @character.pre_run
        # async def command_pre_run(self, context, *args, **kwargs):
        #         print("I ran before the command did!")


def setup(bot):
       Charakter(bot)