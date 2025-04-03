# import json
# import requests
import prompt

print("Script started")
product_id = input("Enter product ID: ")
product_title = input("Enter Product Title: ")
description = input("Enter Description: ")
brand = input("Enter Brand: ")
external_url = input("Enter External URL: ")

products = {}

products[product_id] = {
    "title": product_title,
    "asin": product_id,
    "description": description,
    "brand": brand,
    "link": external_url
}
print("\n=== Product Stored Successfully! ===")

# Asking user to fetch details by productId
search_product_id = input("\nEnter Product ID to fetch details: ").strip()
data= '''{
  "request_info": {
    "success": True,
    "credits_used": 364,
    "credits_used_this_request": 1,
    "credits_remaining": 136,
    "credits_reset_at": "2025-04-04T14:18:25.000Z"
  },
  "request_parameters": {
    "amazon_domain": "amazon.com",
    "asin": "B0CSZ9RZY1",
    "type": "product"
  },
  "request_metadata": {
    "created_at": "2025-03-19T10:24:54.929Z",
    "processed_at": "2025-03-19T10:24:59.412Z",
    "total_time_taken": 4.48,
    "amazon_url": "https://www.amazon.com/dp/B0CSZ9RZY1?th=1&psc=1"
  },
  "product": {
    "title": "SKLZ 5-Position Tee and Impact Practice Balls 12 Pack Bundle, A Comprehensive Training Kit That Can Help You Improve Your Batting Skills.",
    "search_alias": {
      "title": "Sports & Outdoors",
      "value": "sporting"
    },
    "keywords": "SKLZ,5-Position,Tee,and,Impact,Practice,Balls,12,Pack,Bundle,A,Comprehensive,Training,Kit,That,Can,Help,You,Improve,Your,Batting,Skills.",
    "keywords_list": [
      "SKLZ",
      "5-Position",
      "Impact",
      "Practice",
      "Balls",
      "Pack",
      "Bundle",
      "Comprehensive",
      "Training",
      "That",
      "Help",
      "Improve",
      "Your",
      "Batting",
      "Skills."
    ],
    "is_collection": False,
    "asin": "B0CSZ9RZY1",
    "link": "https://www.amazon.com/SKLZ-5-Position-Practice-Comprehensive-Training/dp/B0CSZ9RZY1",
    "brand": "SKLZ",
    "sell_on_amazon": False,
    "proposition_65_warning": True,
    "has_size_guide": True,
    "categories": [
      {
        "name": "Sports & Outdoors",
        "link": "https://www.amazon.com/sports-outdoors/b/ref=dp_bc_1?ie=UTF8&node=3375251",
        "category_id": "3375251"
      },
      {
        "name": "Sports",
        "link": "https://www.amazon.com/Sports-Fitness/b/ref=dp_bc_2?ie=UTF8&node=10971181011",
        "category_id": "10971181011"
      },
      {
        "name": "Team Sports",
        "link": "https://www.amazon.com/team-sports/b/ref=dp_bc_3?ie=UTF8&node=706809011",
        "category_id": "706809011"
      },
      {
        "name": "Baseball",
        "link": "https://www.amazon.com/b/ref=dp_bc_4?ie=UTF8&node=19574751011",
        "category_id": "19574751011"
      },
      {
        "name": "Training Equipment",
        "link": "https://www.amazon.com/Rawlings-Demarini/b/ref=dp_bc_5?ie=UTF8&node=3396431",
        "category_id": "3396431"
      },
      {
        "name": "Batting Tees",
        "link": "https://www.amazon.com/Baseball-Softball-Batting-Tees/b/ref=dp_bc_6?ie=UTF8&node=3395831",
        "category_id": "3395831"
      }
    ],
    "categories_flat": "Sports & Outdoors > Sports > Team Sports > Baseball > Training Equipment > Batting Tees",
    "description": "The SKLZ 5-Position Tee and Impact Practice Balls Bundle is a perfect training kit for baseball enthusiasts. The bundle includes a SKLZ 5-Position Tee and a 12-pack of Impact Practice Baseballs. The tee allows practice for outside, middle, and inside pitches to improve swing mechanics. The tee height can be adjusted from 20 inches to 34 inches. The impact practice baseballs are constructed with proprietary pop-back material that collapses on contact without cracking. The heavy-duty build of the balls provides an authentic feel when hitting. The tee and ball bundle is available at one low price . The tee is designed to improve baseball swing mechanics, fundamentals, and body positioning. The tee stem stores in the center of the plate for easy and compact storage. The pop-back ball design is constructed to collapse on contact without cracking. Perfect your swing with this bundle and take your baseball game to the next level!",
    "sub_title": {
      "text": "Visit the SKLZ Store",
      "link": "https://www.amazon.com/stores/SKLZ/page/37D0D1E9-5BAD-4E94-8740-A288C822F7CA?ref_=ast_bln&store_ref=bl_ast_dp_brandLogo_sto"
    },
    "marketplace_id": "ATVPDKIKX0DER",
    "rating": 5,
    "rating_breakdown": {
      "five_star": {
        "percentage": 100,
        "count": 3
      },
      "four_star": {
        "percentage": 0,
        "count": 0
      },
      "three_star": {
        "percentage": 0,
        "count": 0
      },
      "two_star": {
        "percentage": 0,
        "count": 0
      },
      "one_star": {
        "percentage": 0,
        "count": 0
      }
    },
    "ratings_total": 3,
    "main_image": {
      "link": "https://m.media-amazon.com/images/I/81T4IanslqL.jpg"
    },
    "images": [
      {
        "link": "https://m.media-amazon.com/images/I/81T4IanslqL._AC_SL1500_.jpg",
        "variant": "MAIN"
      },
      {
        "link": "https://m.media-amazon.com/images/I/91vpF2ChtYL._AC_SL1500_.jpg",
        "variant": "PT01"
      },
      {
        "link": "https://m.media-amazon.com/images/I/91KnmRn-fXL._AC_SL1500_.jpg",
        "variant": "PT02"
      },
      {
        "link": "https://m.media-amazon.com/images/I/71AlG3ZlFxL._AC_SL1500_.jpg",
        "variant": "PT03"
      },
      {
        "link": "https://m.media-amazon.com/images/I/61JwYdKjaKL._AC_SL1500_.jpg",
        "variant": "PT04"
      },
      {
        "link": "https://m.media-amazon.com/images/I/61MSfvGE85L._AC_SL1500_.jpg",
        "variant": "PT05"
      },
      {
        "link": "https://m.media-amazon.com/images/I/71sgZkXN9EL._AC_SL1500_.jpg",
        "variant": "PT06"
      }
    ],
    "images_count": 7,
    "images_flat": "https://m.media-amazon.com/images/I/81T4IanslqL._AC_SL1500_.jpg,https://m.media-amazon.com/images/I/91vpF2ChtYL._AC_SL1500_.jpg,https://m.media-amazon.com/images/I/91KnmRn-fXL._AC_SL1500_.jpg,https://m.media-amazon.com/images/I/71AlG3ZlFxL._AC_SL1500_.jpg,https://m.media-amazon.com/images/I/61JwYdKjaKL._AC_SL1500_.jpg,https://m.media-amazon.com/images/I/61MSfvGE85L._AC_SL1500_.jpg,https://m.media-amazon.com/images/I/71sgZkXN9EL._AC_SL1500_.jpg",
    "has_360_view": False,
    "is_bundle": False,
    "feature_bullets": [
      "Includes a 5 Position Tee and a 12 pack of Impact Practice Baseballs",
      "5 Position Tee allows practice for outside, middle, and inside pitches to improve swing mechanics",
      "Adjust tee height from 20 inch to 34 inch",
      "Impact Practice baseballs are constructed with proprietary pop-back material that collapses on contact without cracking",
      "Extremely durable and heavier than traditional pracitce balls for a more realistic feel"
    ],
    "feature_bullets_count": 5,
    "feature_bullets_flat": "Extremely durable and heavier than traditional pracitce balls for a more realistic feel. Impact Practice baseballs are constructed with proprietary pop-back material that colapses on contact without cracking. Adjust tee height from 20 inch to 34 inch. 5 Position Tee allows practice for outside, middle, and inside pitches to improve swing mechanics. Includes a 5 Position Tee and a 12 pack of Impact Practice Baseballs.",
    "buybox_winner": {
      "maximum_order_quantity": {
        "value": 30,
        "hard_maximum": True
      },
      "subscribe_and_save": {
        "base_discount_percentage": 0,
        "tiered_discount_percentage": 5,
        "delivery_message": "Save up to 5% on auto-deliveries.",
        "default_delivery": "3 months (Most common)"
      },
      "new_offers_count": 2,
      "new_offers_from": {
        "symbol": "$",
        "value": 69.99,
        "currency": "USD",
        "raw": "$69.99"
      },
      "is_prime": True,
      "is_prime_exclusive_deal": False,
      "is_amazon_fresh": False,
      "condition": {
        "is_new": True
      },
      "availability": {
        "type": "in_stock",
        "raw": "Only 20 left in stock (more on the way).",
        "dispatch_days": 1,
        "stock_level": 20
      },
      "fulfillment": {
        "type": "1p",
        "standard_delivery": {
          "date": "Monday, March 24",
          "name": "FREE"
        },
        "fastest_delivery": {
          "date": "Saturday, March 22",
          "name": "Or Prime members get FREE delivery Saturday, March 22. Order within 17 hrs 5 mins. Join Prime (function(f) {var _np=(window.P._namespace(\"\"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) { P.when('ready').execute(\"npa-prime-signup-ingress\", () => { P.load.js(\"https://d1nruqhae353qc.cloudfront.net/primesignup/widget.js\"); }); }));"
        },
        "is_sold_by_amazon": True,
        "amazon_seller": {
          "name": "Amazon"
        },
        "is_fulfilled_by_amazon": True,
        "is_fulfilled_by_third_party": False,
        "is_sold_by_third_party": False
      },
      "price": {
        "symbol": "$",
        "value": 69.99,
        "currency": "USD",
        "raw": "$69.99"
      },
      "shipping": {
        "raw": "FREE"
      }
    },
    "specifications": [
      {
        "name": "Brand",
        "value": "‎SKLZ"
      },
      {
        "name": "Material",
        "value": "‎Plastic"
      },
      {
        "name": "Color",
        "value": "‎Black and Yellow"
      },
      {
        "name": "Age Range (Description)",
        "value": "‎Adult"
      },
      {
        "name": "Sport",
        "value": "‎Baseball"
      },
      {
        "name": "Number of Items",
        "value": "‎12"
      },
      {
        "name": "UPC",
        "value": "‎096506144812"
      },
      {
        "name": "Item Package Dimensions L x W x H",
        "value": "‎20.05 x 18.05 x 6.05 inches"
      },
      {
        "name": "Package Weight",
        "value": "‎4.51 Kilograms"
      },
      {
        "name": "Brand Name",
        "value": "‎SKLZ"
      },
      {
        "name": "Warranty Description",
        "value": "‎1 Year Manufacturer"
      },
      {
        "name": "Model Name",
        "value": "‎Tee and Training Ball Bundle"
      },
      {
        "name": "Suggested Users",
        "value": "‎unisex-adult"
      },
      {
        "name": "Manufacturer",
        "value": "‎SKLZ"
      },
      {
        "name": "Style",
        "value": "‎Tee And Ball Bundle"
      },
      {
        "name": "Included Components",
        "value": "‎5 Position Tee, 12 Pack Impact Practice Baseballs"
      },
      {
        "name": "ASIN",
        "value": "B0CSZ9RZY1"
      },
      {
        "name": "Customer Reviews",
        "value": "5.0    5.0 out of 5 stars         3 ratings            var dpAcrHasRegisteredArcLinkClickAction;     P.when('A', 'ready').execute(function(A) {      if (dpAcrHasRegisteredArcLinkClickAction !== true) {       dpAcrHasRegisteredArcLinkClickAction = true;       A.declarative(        'acrLink-click-metrics', 'click',        { \"allowLinkDefault\": true },        function (event) {         if (window.ue) {          ue.count(\"acrLinkClickCount\", (ue.count(\"acrLinkClickCount\") || 0) + 1);         }        }       );      }     });            P.when('A', 'cf').execute(function(A) {    A.declarative('acrStarsLink-click-metrics', 'click', { \"allowLinkDefault\" : true }, function(event){     if(window.ue) {      ue.count(\"acrStarsLinkWithPopoverClickCount\", (ue.count(\"acrStarsLinkWithPopoverClickCount\") || 0) + 1);     }    });   });       5.0 out of 5 stars"
      },
      {
        "name": "Best Sellers Rank",
        "value": "#747,705 in Sports & Outdoors (See Top 100 in Sports & Outdoors) #228 in Baseball & Softball Batting Tees"
      },
      {
        "name": "Date First Available",
        "value": "January 22, 2024"
      },
      {
        "name": "Brand",
        "value": "SKLZ"
      },
      {
        "name": "Material",
        "value": "Plastic"
      },
      {
        "name": "Color",
        "value": "Black and Yellow"
      },
      {
        "name": "Age Range (Description)",
        "value": "Adult"
      },
      {
        "name": "Sport",
        "value": "Baseball"
      }
    ],
    "specifications_flat": "Sport: Baseball. Age Range (Description): Adult. Color: Black and Yellow. Material: Plastic. Brand: SKLZ. Date First Available: January 22, 2024. Best Sellers Rank: #747,705 in Sports & Outdoors (See Top 100 in Sports & Outdoors) #228 in Baseball & Softball Batting Tees. Customer Reviews: 5.0 out of 5 stars 3 ratings 5.0 out of 5 stars. ASIN: B0CSZ9RZY1. Included Components: ‎5 Position Tee, 12 Pack Impact Practice Baseballs. Style: ‎Tee And Ball Bundle. Manufacturer: ‎SKLZ. Suggested Users: ‎unisex-adult. Model Name: ‎Tee and Training Ball Bundle. Warranty Description: ‎1 Year Manufacturer. Brand Name: ‎SKLZ. Package Weight: ‎4.51 Kilograms. Item Package Dimensions L x W x H: ‎20.05 x 18.05 x 6.05 inches. UPC: ‎096506144812. Number of Items: ‎12. Sport: ‎Baseball. Age Range (Description): ‎Adult. Color: ‎Black and Yellow. Material: ‎Plastic. Brand: ‎SKLZ.",
    "bestsellers_rank": [
      {
        "category": "Sports & Outdoors",
        "rank": 747705,
        "link": "https://www.amazon.com/gp/bestsellers/sporting-goods/ref=pd_zg_ts_sporting-goods"
      },
      {
        "category": "Baseball & Softball Batting Tees",
        "rank": 228,
        "link": "https://www.amazon.com/gp/bestsellers/sporting-goods/3395831/ref=pd_zg_hrsr_sporting-goods"
      }
    ],
    "color": "‎Black and Yellow",
    "material": "‎Plastic",
    "manufacturer": "‎SKLZ",
    "first_available": {
      "raw": "January 22, 2024",
      "utc": "2024-01-22T00:00:00.000Z"
    },
    "bestsellers_rank_flat": "Category: Sports & Outdoors | Rank: 747705, Category: Baseball & Softball Batting Tees | Rank: 228"
  },
  "brand_store": {
    "id": "37D0D1E9-5BAD-4E94-8740-A288C822F7CA",
    "link": "https://www.amazon.com/stores/SKLZ/page/37D0D1E9-5BAD-4E94-8740-A288C822F7CA"
  },
  "frequently_bought_together": {
    "total_price": {
      "symbol": "$",
      "value": 110.36,
      "currency": "USD",
      "raw": "$110.36"
    },
    "products": [
      {
        "asin": "B0CSZ9RZY1",
        "title": "SKLZ 5-Position Tee and Impact Practice Balls 12 Pack Bundle, A Comprehensive Training Kit That Can Help You Improve Your Batting Skills.",
        "link": "https://www.amazon.com/dp/B0CSZ9RZY1",
        "image": "https://images-na.ssl-images-amazon.com/images/I/81T4IanslqL._AC_UL116_SR116,116_.jpg",
        "price": {
          "symbol": "$",
          "value": 69.99,
          "currency": "USD",
          "raw": "$69.99"
        }
      },
      {
        "asin": "B07TLPWDPM",
        "title": "SKLZ Premium Impact Limited-Flight Training Baseballs, Perfect for Adding Power to Swing, Use Indoors Or Outdoors for Practice and Drills, Baseball, Softball, and Mini Balls, Yellow/Black",
        "link": "https://www.amazon.com/dp/B07TLPWDPM",
        "image": "https://images-na.ssl-images-amazon.com/images/I/71KqZvsG1xL._AC_UL116_SR116,116_.jpg",
        "price": {
          "symbol": "$",
          "value": 20.38,
          "currency": "USD",
          "raw": "$20.38"
        }
      },
      {
        "asin": "B07RJZLQY7",
        "title": "GoSports Weighted Training Balls - Choose Baseball or Softball - Hitting & Pitching Training for All Skill Levels - Improve Power and Mechanics",
        "link": "https://www.amazon.com/dp/B07RJZLQY7",
        "image": "https://images-na.ssl-images-amazon.com/images/I/71ungmeZFbL._AC_UL116_SR116,116_.jpg",
        "price": {
          "symbol": "$",
          "value": 19.99,
          "currency": "USD",
          "raw": "$19.99"
        }
      }
    ]
  },
  "similar_to_consider": {
    "asin": "B01CKHE45W",
    "link": "https://www.amazon.com/dp/B01CKHE45W/ref=vp_d_pb_TIER4_trans_lp_B0CSZ9RZY1_pd?_encoding=UTF8&pf_rd_p=06cefaa5-a79e-433d-923a-f4250e24166d&pf_rd_r=7169CQRTG49CHE6KDNEW&pd_rd_wg=UMS0c&pd_rd_i=B01CKHE45W&pd_rd_w=G2sue&content-id=amzn1.sym.06cefaa5-a79e-433d-923a-f4250e24166d&pd_rd_r=6b87079d-7b4f-4639-ab13-5bd1a83d065f&psc=1",
    "title": "Amazon Basics Weighted Medicine Ball",
    "rating": 5,
    "ratings_total": 12938,
    "image": "https://m.media-amazon.com/images/I/81vKyC-7TEL._SS100_.jpg",
    "is_prime": True
  },
  "also_bought": [
    {
      "title": "Rope Bat - The Ultimate Hitting System - Baseball & Softball Swing Trainer, Training Tool, Batting Aid",
      "asin": "B01LXO616B",
      "link": "https://www.amazon.com/Rope-Bat-Ultimate-Smushballs-Baseball/dp/B01LXO616B/ref=sims_dp_d_dex_popular_subs_t3_v6_d_sccl_2_1/145-7449583-3388537?pd_rd_w=XpW3O&content-id=amzn1.sym.23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_p=23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_r=7169CQRTG49CHE6KDNEW&pd_rd_wg=urO5K&pd_rd_r=be38674d-7456-4c80-9b15-4d54cda846e8&pd_rd_i=B01LXO616B&psc=1",
      "image": "https://images-na.ssl-images-amazon.com/images/I/71J5fR1r68L._AC_UL165_SR165,165_.jpg",
      "rating": 4.6,
      "ratings_total": 938,
      "price": {
        "symbol": "$",
        "value": 134.95,
        "currency": "USD",
        "raw": "$134.95"
      }
    },
    {
      "title": "PowerNet Crusher & Micro Crusher Training Baseballs & Softballs, Baseball & Softball Hitting Trainer for Improved Speed, Powe",
      "asin": "B07MZDS842",
      "link": "https://www.amazon.com/PowerNet-Crushers-Training-Baseballs-Direction/dp/B07MZDS842/ref=sims_dp_d_dex_popular_subs_t3_v6_d_sccl_2_2/145-7449583-3388537?pd_rd_w=XpW3O&content-id=amzn1.sym.23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_p=23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_r=7169CQRTG49CHE6KDNEW&pd_rd_wg=urO5K&pd_rd_r=be38674d-7456-4c80-9b15-4d54cda846e8&pd_rd_i=B07MZDS842&psc=1",
      "image": "https://images-na.ssl-images-amazon.com/images/I/712YYh9YmuL._AC_UL165_SR165,165_.jpg",
      "rating": 4.6,
      "ratings_total": 1046,
      "price": {
        "symbol": "$",
        "value": 44.99,
        "currency": "USD",
        "raw": "$44.99"
      }
    },
    {
      "title": "Tebery 12 Pack Yellow Dimpled Practice Balls, 12-Inch Pitching Machine Softballs Baseballs for Hand-Eye Coordination, Hitting",
      "asin": "B09X9MYMQT",
      "link": "https://www.amazon.com/Tebery-Sting-Free-Softballs-Baseballs-Coordination/dp/B09X9MYMQT/ref=sims_dp_d_dex_popular_subs_t3_v6_d_sccl_2_3/145-7449583-3388537?pd_rd_w=XpW3O&content-id=amzn1.sym.23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_p=23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_r=7169CQRTG49CHE6KDNEW&pd_rd_wg=urO5K&pd_rd_r=be38674d-7456-4c80-9b15-4d54cda846e8&pd_rd_i=B09X9MYMQT&psc=1",
      "image": "https://images-na.ssl-images-amazon.com/images/I/91h-nTp2T6L._AC_UL165_SR165,165_.jpg",
      "rating": 4.6,
      "ratings_total": 32,
      "price": {
        "symbol": "$",
        "value": 32.99,
        "currency": "USD",
        "raw": "$32.99"
      }
    },
    {
      "title": "Furypiont Baseball Softball Hitting/Batting Tee,Adjustable Height Teeball Tee for Kids and Youth with Bonus Plastic Training ",
      "asin": "B0CZF9RHZP",
      "link": "https://www.amazon.com/Furypiont-Baseball-Softball-Adjustable-Training/dp/B0CZF9RHZP/ref=sims_dp_d_dex_popular_subs_t3_v6_d_sccl_2_4/145-7449583-3388537?pd_rd_w=XpW3O&content-id=amzn1.sym.23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_p=23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_r=7169CQRTG49CHE6KDNEW&pd_rd_wg=urO5K&pd_rd_r=be38674d-7456-4c80-9b15-4d54cda846e8&pd_rd_i=B0CZF9RHZP&psc=1",
      "image": "https://images-na.ssl-images-amazon.com/images/I/61GC+X84RBL._AC_UL165_SR165,165_.jpg",
      "rating": 4.2,
      "ratings_total": 40,
      "price": {
        "symbol": "$",
        "value": 27.99,
        "currency": "USD",
        "raw": "$27.99"
      }
    },
    {
      "title": "GoSports Weighted Training Balls - Choose Baseball or Softball - Hitting & Pitching Training for All Skill Levels - Improve P",
      "asin": "B09K22VD6P",
      "link": "https://www.amazon.com/GoSports-3-82-Weighted-Training-Softballs/dp/B09K22VD6P/ref=sims_dp_d_dex_popular_subs_t3_v6_d_sccl_2_5/145-7449583-3388537?pd_rd_w=XpW3O&content-id=amzn1.sym.23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_p=23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_r=7169CQRTG49CHE6KDNEW&pd_rd_wg=urO5K&pd_rd_r=be38674d-7456-4c80-9b15-4d54cda846e8&pd_rd_i=B09K22VD6P&psc=1",
      "image": "https://images-na.ssl-images-amazon.com/images/I/71JyLUKKJZL._AC_UL165_SR165,165_.jpg",
      "rating": 4.8,
      "ratings_total": 9312,
      "price": {
        "symbol": "$",
        "value": 27.99,
        "currency": "USD",
        "raw": "$27.99"
      }
    },
    {
      "title": "GKK 12 Pack Pitching Machine Softballs,12-Inch Pitching Machine Softballs for Hand-Eye Coordination, Hitting and Fielding Pra",
      "asin": "B0BB8WNVWL",
      "link": "https://www.amazon.com/GKK-Pitching-Softballs-Sting-Free-Coordination/dp/B0BB8WNVWL/ref=sims_dp_d_dex_popular_subs_t3_v6_d_sccl_2_6/145-7449583-3388537?pd_rd_w=XpW3O&content-id=amzn1.sym.23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_p=23e3f38e-3b1c-446d-9cce-2cc73f175b99&pf_rd_r=7169CQRTG49CHE6KDNEW&pd_rd_wg=urO5K&pd_rd_r=be38674d-7456-4c80-9b15-4d54cda846e8&pd_rd_i=B0BB8WNVWL&psc=1",
      "image": "https://images-na.ssl-images-amazon.com/images/I/71Ys1I0nTVL._AC_UL165_SR165,165_.jpg",
      "rating": 4.7,
      "ratings_total": 65,
      "price": {
        "symbol": "$",
        "value": 41.39,
        "currency": "USD",
        "raw": "$41.39"
      }
    }
  ]
}
'''
product_details = prompt.fetch_product_details(products, search_product_id)

    # Generate JSON response
response = {"productDetails": product_details}

    # Print final output
print("\n=== Generated JSON Response ===")
print(response)


