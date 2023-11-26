/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/templates/*.{html,js}",
    "./src/static/crc/input.css",
    "./src/layouts/templates/layouts/*.{html,js}",
  ],
  theme: {
    extend: {
      width: {
        800: "800px",
      },
    },
  },
  plugins: [],
};
