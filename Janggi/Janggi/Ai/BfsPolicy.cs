﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Janggi
{
	public class BfsPolicy
	{
		public class Node
		{
			Stones[][] board;
			float rate;
			List<Node> children;
		}
	}
}
