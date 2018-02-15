using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;

namespace vidily
{
    public class RouteConfig
    {
        public static void RegisterRoutes(RouteCollection routes)
        {
            routes.IgnoreRoute("{resource}.axd/{*pathInfo}");

            //custom router
            routes.MapRoute(
                "MoviesByReleaseDate",
                "Movies/released/{year}/{month}",
                new { Controller = "Movies", action = "ByReleaseDate" },
                //this set limits on the amount of characters that are needed
                new { year = @"\d{4}", month = @"\d{2}" }); //@ works as an escape sequence 

            routes.MapRoute(
                name: "Default",
                url: "{controller}/{action}/{id}",
                defaults: new { controller = "Home", action = "Index", id = UrlParameter.Optional }
            );
        }
    }
}
