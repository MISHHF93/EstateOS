export const dictionaries = {
  en: {
    brand: 'EstateOS',
    tagline: 'AI-native real estate operating system',
    cta: 'Launch workspace',
    trust: 'Transparent AI guidance with governed release controls',
  },
  ar: {
    brand: 'EstateOS',
    tagline: 'منصة عقارية أصلية للذكاء الاصطناعي',
    cta: 'افتح مساحة العمل',
    trust: 'إرشادات ذكاء اصطناعي شفافة مع ضوابط إصدار محكومة',
  },
} as const;

export type Locale = keyof typeof dictionaries;
