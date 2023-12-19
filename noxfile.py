# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import nox

ANSIBLE_VERSIONS = {
    "2.14": "ansible-core~=2.14",
    "2.15": "ansible-core~=2.15",
    "2.16": "ansible-core~=2.16",
    "devel": "ansible-core @ https://github.com/ansible/ansible/archive/devel.tar.gz",
}

nox.options.sessions = (
    "pre-commit",
    "sanity(2.16)",
    "units(2.16)",
    "integration(2.16)",
)


@nox.session(name="pre-commit")
def pre_commit(session: nox.Session) -> None:
    session.install("pre-commit")
    session.run("pre-commit", "run", "-a")


@nox.session()
@nox.parametrize("ansible", list(ANSIBLE_VERSIONS), list(ANSIBLE_VERSIONS))
def units(session: nox.Session, ansible: str) -> None:
    session.install(ANSIBLE_VERSIONS[ansible])
    session.run("ansible-test", "units", *session.posargs)


@nox.session()
@nox.parametrize("ansible", list(ANSIBLE_VERSIONS), list(ANSIBLE_VERSIONS))
def integration(session: nox.Session, ansible: str) -> None:
    session.install(ANSIBLE_VERSIONS[ansible])
    session.run("ansible-test", "integration", *session.posargs)


@nox.session()
@nox.parametrize("ansible", list(ANSIBLE_VERSIONS), list(ANSIBLE_VERSIONS))
def sanity(session: nox.Session, ansible: str) -> None:
    session.install(ANSIBLE_VERSIONS[ansible])
    session.run("ansible-test", "sanity", *session.posargs)
