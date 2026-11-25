---
name: react-native-ui
description: >-
  Build React Native screens and components from a design spec: token-driven StyleSheet styling, platform-correct touch targets, safe areas, and accessible labels. Use for iOS/Android apps built with React Native or Expo.
---

# React Native UI

Mobile is not small web. This skill implements designs in React Native with native expectations: 44pt+ targets, safe-area respect, platform conventions, and performance habits (no shadow-heavy, layout-thrashing styles) baked in from the start.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A design spec needs implementing as React Native/Expo screens
- Web components must be re-expressed for native (no hover, no CSS grid)
- An app looks 'like a website in a wrapper' and needs native feel
- Lists, forms, or sheets need correct keyboard and safe-area behavior

## Inputs you work from

- The screen spec, with mobile priority order already decided (see responsive-layout)
- Project setup: Expo or bare RN, navigation library, existing theme file
- Device matrix: smallest Android target, iOS notch/home-indicator presence
- Data shapes and loading patterns (lists are FlatList territory)

## Workflow

1. Translate the spec's web assumptions: hover -> pressed states, CSS grid -> flex rows/wraps, sticky -> sticky headers or bottom bars within safe areas.
2. Set up or reuse the theme object: colors, spacing (4pt), radius, type — imported, never re-declared per screen.
3. Compose screens from primitives (View/Text/Pressable) with StyleSheet.create; dynamic values computed outside the render hot path.
4. Use FlatList/SectionList for anything list-shaped, with keyExtractor from stable ids and getItemLayout when rows are uniform.
5. Handle the keyboard: KeyboardAvoidingView or form scroll, submit behavior, and inputs that never hide behind the keyboard or home indicator.
6. Add accessibility: accessibilityLabel/Role on interactive elements, focus order sane, dynamic type respected (allowFontScaling left on).
7. Verify pressed/disabled/loading states and dark appearance if the theme supports it.

## Rules

- Pressable over TouchableOpacity for new code; pressed state must be visible (opacity or background change).
- Minimum touch target 44x44pt — use hitSlop when the visual must stay small.
- Never hardcode status-bar or notch offsets: SafeAreaView / insets from the library in use.
- Text scales with the OS setting by default; truncating layouts are a bug, not a style.
- Images get explicit dimensions or aspectRatio — no layout jump on load.

## Output

- Screen and component files with themed StyleSheet styling
- List components with keyExtractor and empty/loading states
- Notes on platform differences deliberately handled (or consciously shared)

## Common pitfalls

- Importing web layouts literally: hover states and tiny targets everywhere
- ScrollView around a 500-row list (memory and jank) instead of FlatList
- Fixed heights that explode when users enable larger text

## Quality checklist

- [ ] All touch targets >= 44pt (hitSlop where needed)
- [ ] Safe areas respected top and bottom
- [ ] Lists virtualized with stable keys and empty state
- [ ] Keyboard never covers the active input or the submit action
- [ ] Accessibility labels/roles on all interactive elements

## Bundled files

- `examples/TierCard.tsx` — a gold-standard example to imitate
- `resources/rn-design-translation.md` — checklist / template / reference for this skill
