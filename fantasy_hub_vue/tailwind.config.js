/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
        colors: {
          // "light-bg-primary": "#f2f4f3",
          "light-bg-primary": "#fffdfa",
          "light-border": "rgb(82 82 82 / 15%)",
          "light-icon": "#213547",
          "light-text": "#2B4458",
          "light-blue-icon": "#27B1E6",
        },
        transitionProperty: {
          'top': 'top',
          'bg': 'background-color',
        },
        backgroundImage: {
          'espn': "url('/img/espn.svg')",
          'sleeper': "url('/img/sleeper.svg')",
          'yahoo': "url('/img/yahoo.svg')",
          'gradient-radial':"radial-gradient(50% 50% at 50% 50%,#312e81 0,hsla(0,0%,100%,0) 100%)",
        },
        keyframes: {
          float_tl: {
            '0%': { transform: 'translateY(1.5rem) rotate(6deg)' },
            // '25%': { transform: 'translateY(2rem)' },
            '50%': { transform: 'translateY(2.5rem) rotate(6deg)' },
            // '75%': { transform: 'translateY(2.25rem)' },
            '100%': { transform: 'translateY(1.5rem) rotate(6deg)' },
          },
          float_tr: {
            '0%': { transform: 'translateY(3rem) rotate(-12deg) scaleX(-1) scaleY(1)' },
            // '25%': { transform: 'translateY(2rem)' },
            '50%': { transform: 'translateY(2rem) rotate(-12deg) scaleX(-1) scaleY(1)' },
            // '75%': { transform: 'translateY(2.25rem)' },
            '100%': { transform: 'translateY(3rem) rotate(-12deg) scaleX(-1) scaleY(1)' },
          },
          float_br: {
            '0%': { transform: 'translateY(1rem) rotate(12deg) scaleX(-1) scaleY(1)' },
            // '25%': { transform: 'translateY(2rem)' },
            '33%': { transform: 'translateY(1.5rem) rotate(12deg) scaleX(-1) scaleY(1)' },
            // '75%': { transform: 'translateY(2.25rem)' },
            '66%': { transform: 'translateY(2rem) rotate(12deg) scaleX(-1) scaleY(1)' },
            '100%': { transform: 'translateY(1rem) rotate(12deg) scaleX(-1) scaleY(1)' },
          },
        },
        animation: {
          'floating-helmet-tl': 'float_tl 8s ease-in-out infinite',
          'floating-helmet-tr': 'float_tr 8s ease-in-out infinite',
          'floating-helmet-br': 'float_br 8s ease-in-out infinite',
        },
        scale: {
        '-1': '-1',
        },
        gridTemplateColumns: {
          'fill-40': 'repeat(auto-fill, 10rem)',
        },
    },
    fontFamily: {
      'inter': ['Inter', 'sans-serif'],
      'poppins': ['Poppins', 'sans-serif'],
      'lato': ['Lato', 'sans-serif'],
      'itim': ['Itim', 'cursive'],
      'ember': ['Amazon Ember', 'sans-serif'],
    },
    screens: {
      'sm': '640px',
      'md': '768px',
      'md-lg': '984px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    container: {
      center: true,
      // padding: {
      //   sm: '2rem',
      //   lg: '4rem',
      //   xl: '5rem',
      //   '2xl': '6rem',
      // },
      screens: {
        sm: '600px',
        md: '728px',
        lg: '984px',
        xl: '1240px',
        '2xl': '1496px',
      },
    },
    borderWidth: {
      '0': '0',
      '1': '1px',
      '2': '2px',
      '4': '4px',
    },
  },
  plugins: [require('@headlessui/tailwindcss'),
            require('tailwind-scrollbar')],
}
