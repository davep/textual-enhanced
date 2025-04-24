# textual-enhanced ChangeLog

## v0.13.0

**Released: 2025-04-24**

- Added `tools.History`.
  ([#50](https://github.com/davep/textual-enhanced/pull/50))

## v0.12.0

**Released: 2025-04-17**

- Renamed `ModalInput.search` to `ModalInput.accept_input`.
  ([#43](https://github.com/davep/textual-enhanced/issues/43))
- A `Command`, invoked either by the command palette or by a binding, will
  now always invoke its action; it's no longer necessary to use `@on` as
  well as define the `action_*_command` function.
  ([#47](https://github.com/davep/textual-enhanced/pull/47))
- A `Command` can now have an `ACTION` that is an inline action; it's no
  longer necessary to define one `action_*_command` per command (eg: a
  `Quit` command can set its `ACTION` to `"app.quit"`, etc).
  ([#47](https://github.com/davep/textual-enhanced/pull/47))

## v0.11.0

**Released: 2025-04-03**

- Added <kbd>g</kbd>, <kbd>G</kbd>, <kbd>\<</kbd>, <kbd>></kbd>,
  <kbd>p</kbd> and <kbd>%</kbd> as extra bindings for going home/end in
  `containers.EnhancedVerticalScrol`.
  ([#40](https://github.com/davep/textual-enhanced/pull/40))

## v0.10.0

**Released: 2025-04-01**

- Extended the command system so that Textual's `Keymap` facility can be
  used. ([#36](https://github.com/davep/textual-enhanced/pull/36))
- Dropped support for Python 3.9.

## v0.9.0

**Released: 2025-03-31**

- Added `containers.EnhancedVerticalScroll`.
  ([#33](https://github.com/davep/textual-enhanced/pull/33))

## v0.8.1

**Released: 2025-03-15***

- Made a cosmetic improvement to the binding table in the help screen if
  there are no bindings associated with commands.

## v0.8.0

**Released: 2025-03-15***

- Added the idea of a `HelpfulBinding`.
  ([#27](https://github.com/davep/textual-enhanced/pull/27))

## v0.7.1

**Released: 2025-03-07***

- Added a temporary workaround for Textual 2.0.x's kinda-unannounced
  breaking change to how the command palette works.
  ([#23](https://github.com/davep/textual-enhanced/pull/23))

## v0.7.0

**Released: 2025-03-02***

- Added `maybe` to `CommandsProvider`.

## v0.6.0

**Released: 2025-02-12**

- Added `initial` to `ModalInput`.
  ([#17](https://github.com/davep/textual-enhanced/pull/17))

## v0.5.0

**Released: 2025-02-08**

- Tweaked the styling of the command palette's scrollbar so it's less
  intrusive. ([#14](https://github.com/davep/textual-enhanced/pull/14))
- Added `ChangeTheme` as a common command.
  ([#15](https://github.com/davep/textual-enhanced/pull/15))
- Added handling code for the common commands to `EnhancedScreen`.
  ([#15](https://github.com/davep/textual-enhanced/pull/15))

## v0.4.0

**Released: 2025-02-03**

- Allow forcing `dim` when adding a key with `add_key`.
  ([#11](https://github.com/davep/textual-enhanced/pull/11))
- Added `EnhancedScreen`.
  ([#12](https://github.com/davep/textual-enhanced/pull/12))

## v0.3.0

**Released: 2025-02-03**

- Added `Confirm`. ([#8](https://github.com/davep/textual-enhanced/pull/8))
- Added `add_key`. ([#9](https://github.com/davep/textual-enhanced/pull/9))

## v0.2.0

**Released: 2025-02-02**

- Added `ModalInput`.
  ([#3](https://github.com/davep/textual-enhanced/pull/3))
- Added `HelpScreen`.
  ([#5](https://github.com/davep/textual-enhanced/pull/5))
- Added common command messages and a common command provider.
  ([#5](https://github.com/davep/textual-enhanced/pull/5))

## v0.1.0

**Released: 2025-02-01**

- Initial release.

[//]: # (ChangeLog.md ends here)
