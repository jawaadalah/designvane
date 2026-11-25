<!-- Gold standard — SFC excerpt -->
<script setup lang="ts">
type Tier = { id: string; name: string; price: string; features: string[]; soldOut?: boolean };
const props = defineProps<{ tier: Tier; popular?: boolean }>();
const emit = defineEmits<{ select: [tier: Tier] }>();
</script>

<template>
  <article class="card" :class="{ popular }" :aria-label="`${tier.name} plan`">
    <h3>{{ tier.name }}</h3>
    <p class="price">{{ tier.price }}<span>/mo</span></p>
    <ul><li v-for="f in tier.features" :key="f">{{ f }}</li></ul>
    <button type="button" :disabled="tier.soldOut" @click="emit('select', tier)">
      {{ tier.soldOut ? "Sold out" : `Choose ${tier.name}` }}
    </button>
    <p v-if="tier.soldOut">Back in stock next month.</p>
  </article>
</template>

<style scoped>
.card { padding: var(--space-4); border: 1px solid var(--border); border-radius: var(--radius-lg); }
.card.popular { border-color: var(--accent); }
.price { font-size: var(--text-heading-md); }
</style>
