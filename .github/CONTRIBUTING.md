# Contributing to Sleigh

Contributions are always welcome! No need to sign anything, or do anything, just
submit a PR/issue and go! 🤟

## Code of Conduct

The [Code of Conduct] is something that describes what everyone should do inside
this repository.It's a standard copy-and-paste file, but it boils down to just
being nice and mindful of others and what they might be doing.

## The Discussions (alternatively: I HAVE A QUESTION!!!)

If you just have a question you want answered, don't file an issue. Instead, use
the [Discussions] board I set up. It's a sort-of Discourse, except you probably
already have an account for it, so it's even quicker! Go there right now and ask
your question, and it will be answered by me or someone else! :)

## Filing an Issue

Only file an issue if it's something that doesn't belong / is too major for the
Discussions board (e.g. a bug report or feature request). If your feature idea
isn't quite finished yet, submit it to the Ideas category on the [Discussions]
board.

Now, as for the actual issue, try to **be descriptive** but not *too much*, as
a wall of text can become meaningless quickly. The main guide is to try to get
as much **helpful** information inside of as little text as possible, whilst it
still being **readable** and **understandable**.

If you are filing a bug, use the Bug Report template that pops up when you make
a new issue. It has everything you need, including a title, repro steps and
results.

## Submitting a Pull Request

First of all, if you want to submit a pull request, THANK YOU SO MUCH. By making
a Pull Request, not only have you identified an issue / new feature, you also
FIXED IT YOURSELF, which makes my life easier, and you an awesome person!

If you are looking for code contributions to get started with, check out the
Issues page for some issues you think you could tackle. If they were already
closed, consider looking back to see how the issue was fixed.

When you submit a Pull Request, make sure to mark it as a **draft** until you're
done with all changes. Also add a checklist in the beginning for others to keep
track of your progress. As you change the PR, automated checks will run to make
sure that Sleigh still functions properly. These checks take ~15-20 minutes to
complete, so I recommend committing about that frequently.

Remember: the key with any commits is to do little and many. This will allow the
greatest flexibility in case you need to go back in time when you inevitably do
something wrong. However, **don't spam commits**. There's a fine line between
doing good, little commits, and spamming them.

As you do commits, an automatic formatter bot will format your code with Black,
which will create another commit. Remember to watch the action in GitHub after
you commit, and `git pull` if you need to.

If you do multiple commits inside of the 20 minutes, considering prefixing your
commit with `[ci-skip]` to skip tests if the change is small. (The auto-format
bot does this to save you time)

*To be continued...*

[Code of Conduct]: https://github.com/andre4ik3/sleigh/blob/main/.github/CODE_OF_CONDUCT.md
[Discussions]: https://github.com/andre4ik3/sleigh/discussions
