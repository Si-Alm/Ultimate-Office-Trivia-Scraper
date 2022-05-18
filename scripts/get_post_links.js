// basic asyncrhonous sleep function
function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

// track scraped links
var allLinks = [];

// function to scrape all post links for 
async function scrape() {
	// estimated full page size after loading every post
	//   a little bit of trial and error might be needed to get it right - tho going too high won't really hurt
	let pageSize = 112400;

	// keep scrolling the page until we hit around where the bottom is (i.e until every post in the account has made an appearance)
	while (document.body.scrollHeight < pageSize) {
		// get all links currently on page
		let links = document.getElementsByTagName("a");

		// add all links to posts to the allLinks array
		for (let i = 0; i < links.length; i++) {
			if (links[i].href.indexOf("/p/") !== -1)
				allLinks.push(links[i].href);
		}
		// note how many links were found
		console.log("Found " + links.length + " links");

		// very short sleep before scrolling to make sure everything got scraped (js is asynchronous)
		await sleep(10);

		// scroll to the bottom of the page (i.e. load more links)
		window.scrollTo(0, document.body.scrollHeight);

		// quick sleep to let posts load
		await sleep(1500);

	}
}

// call function to scrape links
scrape();

// remove any duplicate links
//  this array can then be inspected in the console to retrieve post linkss
var allLinks = [...new Set(allLinks)];