<!--
Copyright (C) 2023 Ansible Project
Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
SPDX-License-Identifier: GPL-3.0-or-later
-->

# gotmax23.sourcehut

[![CI](https://github.com/gotmax23/ansible-collection-sourcehut/workflows/CI/badge.svg?event=push)](https://github.com/ansible-collections/ansible-collection-sourcehut/actions)

This Ansible collection provides modules and plugins to interact with the
sourcehut API.

## Code of Conduct

We follow the [Ansible Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html) in all our interactions within this project.

If you encounter abusive behavior, please refer to the [policy violations](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html#policy-violations) section of the Code for information on how to raise a complaint.

## Communication

We announce important development changes and releases through Ansible's [The Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn). If you are a collection developer, be sure you are subscribed.

Join us on:
* The Ansible forum:
    * [News & Announcements](https://forum.ansible.com/c/news/5/none)
    * [Get Help](https://forum.ansible.com/c/help/6/none)
    * [Social Spaces](https://forum.ansible.com/c/chat/4)
* Matrix chat rooms:
    * [#users:ansible.com](https://matrix.to/#/#users:ansible.com): general use questions and support
    * [#community:ansible.com](https://matrix.to/#/#community:ansible.com): community and collection development questions
    * [#social:ansible.com](https://matrix.to/#/#social:ansible.com): to say "Good morning, community!"

For more information about communication, refer to the [Ansible communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).

## Contributing to this collection

The content of this collection is made by people like you, a community of individuals collaborating on making the world better through developing automation software.

We are actively accepting new contributors and all types of contributions are very welcome.

Don't know how to start? Refer to the [Ansible community guide](https://docs.ansible.com/ansible/devel/community/index.html)!

Want to submit code changes? Take a look at the [Quick-start development guide](https://docs.ansible.com/ansible/devel/community/create_pr_quick_start.html).

We also use the following guidelines:

* [Collection review checklist](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_reviewing.html)
* [Ansible development guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
* [Ansible collection development guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections)

## Collection maintenance

The current maintainers are listed in the [MAINTAINERS.md](MAINTAINERS.md) file. If you have questions or need help, feel free to mention them in the proposals.

To learn how to maintain/become a maintainer of this collection, refer to the [Maintainer guidelines](https://docs.ansible.com/ansible/devel/community/maintainers.html).

It is necessary for maintainers of this collection to be subscribed to:

* The collection itself (the `Watch` button -> `All Activity` in the upper right corner of the repository's homepage).
* The [news-for-maintainers repository](https://github.com/ansible-collections/news-for-maintainers).

They also should be subscribed to Ansible's [The Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn).

## Governance

The process of decision making in this collection is based on discussing and finding consensus among participants.

Every voice is important. If you have something on your mind, create an issue or dedicated discussion and let's discuss it!

## Tested with Python

These modules are meant to be run from the Ansible controller and are only
tested on the controller Python versions. See the next section for the
supported Python and ansible-core versions.

## Tested with ansible-core

- 2.14 (Python 3.9, 3.10, 3.11)
- 2.15 (Python 3.9, 3.10, 3.11)
- 2.16 (Python 3.10, 3.11, 3.12)

## External requirements

- [The `sourcehutx` Python library](https://pypi.org/project/sourcehutx)


## Included content

TODO

## Using this collection

TODO

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:
```bash
ansible-galaxy collection install gotmax23.sourcehut
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```yaml
---
collections:
  - name: gotmax23.sourcehut
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:

```bash
ansible-galaxy collection install gotmax23.sourcehut --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `0.1.0`:

```bash
ansible-galaxy collection install gotmax23.sourcehut:==0.1.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Release notes

See the [changelog](https://github.com/ansible-collections/REPONAMEHERE/tree/main/CHANGELOG.rst).

## More information


- [Ansible user guide](https://docs.ansible.com/ansible/devel/user_guide/index.html)
- [Ansible developer guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
- [Ansible collections requirements](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html)
- [Ansible community Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
- [The Bullhorn (the Ansible contributor newsletter)](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn)
- [Important announcements for maintainers](https://github.com/ansible-collections/news-for-maintainers)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSES/GPL-3.0-or-later.txt](LICENSES/GPL-3.0-or-later.txt]) to see the full text.
