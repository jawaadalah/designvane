# Web design -> React Native translation

| Web assumption        | Native equivalent |
|-----------------------|-------------------|
| hover state           | pressed state on Pressable |
| CSS grid              | flexDirection row + flexWrap, or column lists |
| position: sticky      | stickyHeaderIndices / bottom bar in safe area |
| box-shadow            | elevation (Android) + shadow props (iOS), sparingly |
| 16px body text        | 16pt, allowFontScaling stays ON |
| click                 | onPress, min target 44x44pt (hitSlop) |
| tooltip               | long-press hint or inline helper text |
| media queries         | useWindowDimensions breakpoints for tablets |

Always test: smallest Android in the matrix, largest iOS text size.
