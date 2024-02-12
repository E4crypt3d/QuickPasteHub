/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./templates/*.html", "./templates/partials/*.html"],
	daisyui: {
		themes: ["retro", "night"],
	},
	plugins: [require("daisyui")],
};
