/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./templates/*.html", "./templates/partials/*.html"],
	daisyui: {
		themes: ["dark"],
	},
	plugins: [require("daisyui")],
};
