const apiKey = "PDZMhvoaOkr2HcU1Eto50vgxAa0sJjmk7G1EyjcB5UPXA9-ZBzA_XjSGuoE7M6FeJuzzXZGN-NjFIzYPyL4dKQawFpklYd3Rp18KhKr4AE-DFu0IUKM3HN1EyMrvX3Yx";

const Yelp = {
  searchYelp(term, location, sortBy) {
    return fetch(`https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?term=${term}&location=${location}&sort_by=${sortBy}`, {
        headers: {
            Authorization: `Bearer ${apiKey}`,
        }
    }).then(response => {
        return response.json();
    }).then(jsonResponse => {
        if (jsonResponse.businesses) {
            return jsonResponse.businesses.map(business => ({
              id: business.id,
              imageSrc: business.image_url,
              name: business.name,
              address: business.location.address1,
              city: business.location.city,
              state: business.location.state,
              zipCode: business.location.zip_code,
              category: business.categories[0].title,
              rating: business.rating,
              reviewCount: business.review_count
            }));
        }
    })
  }  
};

export default Yelp;
