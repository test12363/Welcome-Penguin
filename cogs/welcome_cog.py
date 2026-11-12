# Penguin Welcome Cog - Made by 6YuaZ
# Feel free to tweak the embed text or colors below to match your server's vibe!

import json
import discord
from discord.ext import commands
from datetime import datetime, timezone

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Grabbing your channel IDs from the config
        with open("welcome_config.json", "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def build_welcome_embed(self, member):
        verify_id = self.config["verify_channel_id"]
        support_id = self.config["support_channel_id"]

        # You can change the title, description, or hex color (0x2B2D31) right here
        embed = discord.Embed(
            title="🐧 Welcome to the Igloo!",
            description=(
                f"Hey {member.mention}, welcome to **{member.guild.name}**!\n\n"
                f"• Verify yourself in <#{verify_id}> to unlock all channels\n"
                f"• Need help? Open a ticket in <#{support_id}>\n"
                "• Enjoy your stay with the Penguin community!"
            ),
            color=0x2B2D31,
            timestamp=datetime.now(timezone.utc)
        )
        
        # Shows the new member's avatar on the top right
        embed.set_thumbnail(url=member.display_avatar.url)
        
        # Footer with server icon and live member count
        embed.set_footer(
            text=f"Penguin Community • Member #{member.guild.member_count}",
            icon_url=member.guild.icon.url if member.guild.icon else None
        )
        return embed

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # We ignore bots so they don't trigger welcome messages
        if member.bot:
            return

        channel = self.bot.get_channel(self.config["welcome_channel_id"])
        if channel is None:
            print("[ERROR] Couldn't find the welcome channel. Double-check your ID in welcome_config.json!")
            return

        embed = self.build_welcome_embed(member)
        await channel.send(content=f"{member.mention}", embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def testwelcome(self, ctx):
        """Admin-only command to preview the welcome message without waiting for someone to join"""
        channel = self.bot.get_channel(self.config["welcome_channel_id"])
        if channel is None:
            await ctx.send("❌ Welcome channel not found. Check your ID in `welcome_config.json`.")
            return

        embed = self.build_welcome_embed(ctx.author)
        await channel.send(content=f"{ctx.author.mention}", embed=embed)
        await ctx.message.add_reaction("✅")

async def setup(bot):
    await bot.add_cog(WelcomeCog(bot))
