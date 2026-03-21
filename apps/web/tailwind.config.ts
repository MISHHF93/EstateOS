import type { Config } from 'tailwindcss';

export default {
  content: [
    './app/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './lib/**/*.{ts,tsx}',
    './providers/**/*.{ts,tsx}',
    './stores/**/*.{ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        surface: '#08111f',
        panel: '#0f1a2f',
        accent: '#5eead4',
        ink: '#e2e8f0',
        success: '#22c55e',
        warning: '#f59e0b',
        danger: '#f97316',
      },
      boxShadow: {
        glow: '0 24px 80px rgba(34, 211, 238, 0.12)',
      },
      backgroundImage: {
        aurora:
          'radial-gradient(circle at top left, rgba(94,234,212,0.18), transparent 30%), radial-gradient(circle at top right, rgba(59,130,246,0.15), transparent 28%), linear-gradient(180deg, #08111f 0%, #050914 100%)',
      },
    },
  },
  plugins: [],
} satisfies Config;
