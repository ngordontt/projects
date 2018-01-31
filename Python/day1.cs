using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    class Solution
    {
        static void Main(string[] args)
        {

            int i = 4;
            double d = 4.0;
            string s = "HackerRank ";

            List<string> contents = new List<string>();
            string line;

            for (int b = 0; b < 3; b++)
            {
                line = Console.ReadLine();
                contents.Add(line);
            }

            Console.WriteLine(Convert.ToInt16(contents.ElementAt(0)) + i);
            Console.WriteLine(Convert.ToDouble(contents.ElementAt(1)) + d);
            Console.WriteLine(s + contents.ElementAt(2));

        }
    }
}
