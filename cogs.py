from discord.ext import commands
from discord.ext.commands import BucketType
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

from lichess import LichessHTTP

from embeds import NewGameEmbed

class Game(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.lichess = LichessHTTP()

  @commands.guild_only()
  @commands.cooldown(5, 30, BucketType.user)
  @cog_ext.cog_subcommand(
    base="game", 
    description = "challenge another player to a lichess game",
    options = [
      create_option(
        name="white",
        description="assign the white player",
        option_type=6,
        required=True   
      ),
      create_option(
        name="black",
        description="assign the black player",
        option_type=6,
        required=True   
      ),
      create_option(
        name="type",
        description="choose the type of game",
        option_type=3,
        required=False,
        choices = [
          create_choice(
            name="standard",
            value="standard"
          ),
          create_choice(
            name="chess960",
            value="chess960"
          ),
          create_choice(
            name="crazyhouse",
            value="crazyhouse"
          ),
          create_choice(
            name="antichess",
            value="antichess"
          ),
          create_choice(
            name="atomic",
            value="atomic"
          ),
          create_choice(
            name="horde",
            value="horde"
          ),
          create_choice(
            name="kingOfTheHill",
            value="kingOfTheHill"
          ),
          create_choice(
            name="racingKings",
            value="racingKings"
          ),
          create_choice(
            name="threeCheck",
            value="threeCheck"
          ),
        ]
      )   
    ]
    )
  async def create(self, ctx, white, black, varient = "standard"):

    await ctx.defer()

    resp = await self.lichess.create_open_challange(varient)

    white_url = resp.get("urlWhite")
    black_url = resp.get("urlBlack")
    code = resp.get("challenge").get("id")
    recap = resp.get("challenge").get("url")
        
    new_game = NewGameEmbed(white, black, white_url, black_url)
    await ctx.send(embed=new_game.embed)


def setup(bot):
    bot.add_cog(Game(bot))
