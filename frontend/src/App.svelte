<script>
	import { Router, Route } from "svelte-routing";
	import NavLink from "./components/NavLink.svelte";
	import About from "./routes/About.svelte";

	import Blog from "./routes/Blog.svelte";
	import Home from "./routes/Home.svelte";

	export let url = "";

</script>

<main>
	<Router url="{url}">
		<nav class="">
		  <NavLink to="/">Home</NavLink>
		  <NavLink to="about">About</NavLink>
		  <NavLink to="blog">Blog</NavLink>
		</nav>
		<div>
		  <Route path="about" component="{About}" />
		  <Route path="blog" component="{Blog}" />
		  <Route path="/" component="{Home}" />
		</div>
	  </Router>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>