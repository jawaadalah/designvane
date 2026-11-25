// Gold standard — React Native component excerpt
import { Pressable, StyleSheet, Text, View } from "react-native";
import { theme } from "../theme";

type Tier = { id: string; name: string; price: string; soldOut?: boolean };

export function TierCard({ tier, onSelect }: { tier: Tier; onSelect: (t: Tier) => void }) {
  return (
    <View style={styles.card} accessibilityLabel={`${tier.name} plan`}>
      <Text style={styles.name}>{tier.name}</Text>
      <Text style={styles.price}>{tier.price}/mo</Text>
      <Pressable
        accessibilityRole="button"
        accessibilityState={{ disabled: !!tier.soldOut }}
        disabled={tier.soldOut}
        onPress={() => onSelect(tier)}
        style={({ pressed }) => [styles.cta, pressed && styles.ctaPressed]}>
        <Text style={styles.ctaText}>{tier.soldOut ? "Sold out" : `Choose ${tier.name}`}</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: theme.space[4], borderWidth: 1, borderColor: theme.color.border,
          borderRadius: theme.radius.lg, gap: theme.space[2] },
  name: { fontSize: theme.text.headingSm, fontWeight: "600", color: theme.color.ink },
  price: { fontSize: theme.text.headingMd, color: theme.color.ink },
  cta: { minHeight: 48, justifyContent: "center", alignItems: "center",
         backgroundColor: theme.color.accent, borderRadius: theme.radius.md },
  ctaPressed: { opacity: 0.85 },
  ctaText: { color: "#FFFFFF", fontWeight: "600" },
});
