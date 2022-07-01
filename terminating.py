#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-29 15:17:34
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

import typer

existing_usernames = ["rick", "morty"]

def main(username: str):
    maybe_create_user(username=username)
    send_new_notification(username=username)


def maybe_create_user(username: str):
    if username in existing_usernames:
        typer.secho("The user already exists", fg=typer.colors.RED, bg='green')
        raise typer.Exit()
    else:
        typer.echo(f"User created: {username}")


def send_new_notification(username: str):
    typer.secho(f"Notification sent for new user: {username}", fg="black", bg="green")


if __name__ == "__main__":
    typer.run(main)

