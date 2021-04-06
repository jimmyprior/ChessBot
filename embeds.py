from datetime import datetime

from discord import Embed

class NewGameEmbed:

  COLOR = 0xfb29ff
  AUTHOR = "Dedicated Pawn"
  AUTHOR_ICON = "https://i.imgur.com/ZK99yaV.png"
  IMAGE = "https://i.imgur.com/ZnQBxB5.jpeg"

  def __init__(self, white, black, white_url, black_url):
    self.white = white
    self.black = black 
    self.wurl = white_url
    self.burl = black_url

  @property
  def embed(self):
    embed = Embed(
      title = " ", 
      color = self.COLOR,
      timestamp=datetime.utcnow()
    )
    embed.set_author(
      name=self.AUTHOR, 
      icon_url=self.AUTHOR_ICON
    )
    embed.add_field(
      name = "**White Team**", 
      value = f"**{self.white.mention} join __[here]({self.wurl})__**",
      inline=True,
    )
    embed.add_field(
      name = "**Black Team**", 
      value = f"**{self.black.mention} join __[here]({self.burl})__**",
      inline=True,
    )
    #embed.set_thumbnail(url = self.THUMBNAIL)
    embed.set_image(url = self.IMAGE)
    embed.set_footer(text="Good Luck! You Got This!")
    return(embed)