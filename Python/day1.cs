using System;
using System.Collections.Generic;

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

            for (int b = 0; b < 2; b++)
            {
                line = Console.ReadLine();
                contents.Add(line);
            }
            
            foreach (string p in contents)
            {
                Console.WriteLine(p);
            }
            
        }
    }
}
