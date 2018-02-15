using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using vidily.Models;

namespace vidily.ViewModels
{
    public class RandomMovieViewModel
    {
        public Movie Movie { get; set; }
        public List <Customer> Customers { get; set; }

    }
}