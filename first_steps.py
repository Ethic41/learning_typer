#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-06-29 13:41:41
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

import typer


def main(
    name: str, 
    lastname: str, 
    middlename: str = "", 
    formal: bool = False
):
    if formal:
        typer.echo(typer.style(f"Good day Ms. {name} {middlename} {lastname}", \
            fg=typer.colors.RED, bold=True, bg=typer.colors.GREEN))
    else:
        typer.secho(f"Hello {name} {lastname}", fg=typer.colors.MAGENTA)


if __name__ == "__main__":
    typer.run(main)

