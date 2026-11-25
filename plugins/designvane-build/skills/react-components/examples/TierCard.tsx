// Gold standard — component excerpt
import styles from "./TierCard.module.css";

type Tier = {
  name: string; price: string; features: string[];
  popular?: boolean; soldOut?: boolean;
};

const variantClass = { default: "", popular: styles.popular } as const;

export function TierCard({ tier, onSelect }: { tier: Tier; onSelect: (t: Tier) => void }) {
  return (
    <article className={`${styles.card} ${tier.popular ? variantClass.popular : ""}`}
             aria-label={`${tier.name} plan`}>
      <h3>{tier.name}</h3>
      <p className={styles.price}>{tier.price}<span>/mo</span></p>
      <ul>{tier.features.map((f) => <li key={f}>{f}</li>)}</ul>
      <button type="button" disabled={tier.soldOut} onClick={() => onSelect(tier)}
              aria-describedby={tier.soldOut ? "soldout-note" : undefined}>
        {tier.soldOut ? "Sold out" : `Choose ${tier.name}`}
      </button>
      {tier.soldOut && <p id="soldout-note">Back in stock next month.</p>}
    </article>
  );
}
