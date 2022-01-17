{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b4a00a27",
   "metadata": {},
   "source": [
    "My assignment is based on Real Estate Python Library, from the CORGIS Dataset Project. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0bd0cafe",
   "metadata": {},
   "source": [
    "Overview\n",
    "Real Estate Across the United States (REXUS) is the primary tool used by PBS to track and manage the government’s real property assets and to store inventory data, building data, customer data, and lease information. STAR manages aspects of real property space management, including identification of all building space and daily management of 22,000 assignments for all property to its client Federal agencies. This data set contains PBS building inventory that consists of both owned and leased buildings with active and excess status.\n",
    "\n",
    "https://catalog.data.gov/dataset/real-estate-across-the-united-states-rexus-inventory-building"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c66414ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "import real_estate\n",
    "import os as _os\n",
    "import pickle as _pickle\n",
    "# Import datetime class from datetime module\n",
    "from datetime import datetime\n",
    "building = real_estate.get_building()\n",
    "\n",
    "__all__ = ['get_building']\n",
    "__file__ = 'real.py'\n",
    "\n",
    "\n",
    "def _tifa_definitions():\n",
    "    return {\"type\": \"ModuleType\",\n",
    "        \"fields\": {\n",
    "            'get': {\n",
    "                \"type\": \"FunctionType\",\n",
    "                \"name\": 'get',\n",
    "                \"returns\": {\n",
    "                    \"type\": \"ListType\", \n",
    "                    \"empty\": False, \n",
    "                    \"subtype\": {\"type\": \"NumType\"}\n",
    "                }\n",
    "            },\n",
    "            'get_building': {\n",
    "                \"type\": \"FunctionType\",\n",
    "                \"name\": 'get_building',\n",
    "                \"returns\": \n",
    "\t\t\t\t{\"type\": \"ListType\", \"subtype\": \n",
    "\t\t\t\t\t{\"type\": \"DictType\", \"literals\": [{\"type\": \"LiteralStr\", \"value\": 'data'}, {\"type\": \"LiteralStr\", \"value\": 'location'}], \"values\": [\n",
    "\t\t\t\t\t\t{\"type\": \"DictType\", \"literals\": [{\"type\": \"LiteralStr\", \"value\": 'date'}, {\"type\": \"LiteralStr\", \"value\": 'owned or leased'}, {\"type\": \"LiteralStr\", \"value\": 'parking spaces'}, {\"type\": \"LiteralStr\", \"value\": 'status'}, {\"type\": \"LiteralStr\", \"value\": 'type'}, {\"type\": \"LiteralStr\", \"value\": 'disabilities'}], \"values\": [\n",
    "\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t{\"type\": \"NumType\"}, \n",
    "\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t{\"type\": \"DictType\", \"literals\": [{\"type\": \"LiteralStr\", \"value\": 'ADA Accessible'}, {\"type\": \"LiteralStr\", \"value\": 'ansi usable'}], \"values\": [\n",
    "\t\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t\t{\"type\": \"StrType\"}]}]}, \n",
    "\t\t\t\t\t\t{\"type\": \"DictType\", \"literals\": [{\"type\": \"LiteralStr\", \"value\": 'congressional district'}, {\"type\": \"LiteralStr\", \"value\": 'id'}, {\"type\": \"LiteralStr\", \"value\": 'region id'}, {\"type\": \"LiteralStr\", \"value\": 'address'}], \"values\": [\n",
    "\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t{\"type\": \"DictType\", \"literals\": [{\"type\": \"LiteralStr\", \"value\": 'city'}, {\"type\": \"LiteralStr\", \"value\": 'county'}, {\"type\": \"LiteralStr\", \"value\": 'line 1'}, {\"type\": \"LiteralStr\", \"value\": 'state'}, {\"type\": \"LiteralStr\", \"value\": 'zip'}], \"values\": [\n",
    "\t\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t\t{\"type\": \"StrType\"}, \n",
    "\t\t\t\t\t\t\t\t{\"type\": \"StrType\"}]}]}]}}\n",
    "            # returns current date and time\n",
    "                               \n",
    "                },\n",
    "        }\n",
    "    }\n",
    "\n",
    "class _Constants(object):\n",
    "    '''\n",
    "    Global singleton object to hide some of the constants; some IDEs reveal\n",
    "    internal module details very aggressively, and there's no other way\n",
    "    to hide stuff.\n",
    "    '''\n",
    "\n",
    "class DatasetException(Exception):\n",
    "    ''' Thrown when there is an error loading the dataset for some reason.'''\n",
    "    \n",
    "_Constants._DATABASE_NAME = _os.path.join(_os.path.dirname(__file__),\n",
    "                                          \"real_estate.data\")\n",
    "if not _os.access(_Constants._DATABASE_NAME, _os.F_OK):\n",
    "    raise DatasetException((\"Error! Could not find a \\\"{0}\\\" file. \"\n",
    "                           \"Make sure that there is a \\\"{0}\\\" in the \"\n",
    "                           \"same directory as \\\"{1}.py\\\"! Spelling is \"\n",
    "                           \"very important here.\"\n",
    "                           ).format(_Constants._DATABASE_NAME, __name__))\n",
    "elif not _os.access(_Constants._DATABASE_NAME, _os.R_OK):\n",
    "    raise DatasetException((\"Error! Could not read the \\\"{0}\\\" file. \"\n",
    "                            \"Make sure that it readable by changing its \"\n",
    "                            \"permissions. You may need to get help from \"\n",
    "                            \"your instructor.\"\n",
    "                            ).format(_Constants._DATABASE_NAME, __name__))\n",
    "\n",
    "\n",
    "_Constants._DATASET = None\n",
    "\n",
    "def get_building():\n",
    "    \"\"\"\n",
    "    Retrieves all of the building.\n",
    "    \"\"\"\n",
    "    if _Constants._DATASET is None:\n",
    "        with open(_Constants._DATABASE_NAME, 'rb') as _:\n",
    "            _Constants._DATASET = _pickle.load(_)\n",
    "    return _Constants._DATASET\n",
    "\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    from pprint import pprint as _pprint\n",
    "    from timeit import default_timer as _default_timer\n",
    "    \n",
    "    print(\">>> get_building()\")\n",
    "    \n",
    "    start_time = _default_timer()\n",
    "    result = get_building()\n",
    "    print(\"Time taken: {}\".format(_default_timer() - start_time))\n",
    "    _pprint(result[0])\n",
    "    \n",
    "    calc()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "353bea89",
   "metadata": {},
   "source": [
    "Documentation :\n",
    "get_building()\n",
    "Returns a list of dictionaries representing building.\n",
    "Each row represents building."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "c2a4bf1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calc():\n",
    "# returns current date and time\n",
    "    now = datetime.now()\n",
    "    print(\"Present time = \", now)\n",
    "    print(\"Type of the class : \",type(building))\n",
    "    print(\"Number of rows : \",len(building))\n",
    "    print(\"Printing keys : \",building[0].keys())\n",
    "    print(\"Printing values : \",building[0].values())\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "68eb23b9",
   "metadata": {},
   "source": [
    "In this module, we can see that I have a custom function calc that performs certain operations on the dataset. I have used import datetime class from datetime module, to calculate the time at present. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1aa92054",
   "metadata": {},
   "outputs": [],
   "source": [
    "# commands to read the datafile    \n",
    "a=building[0]['data']['date']\n",
    "b=building[0]['location']['congressional district']\n",
    "print(a,b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6bcf968b",
   "metadata": {},
   "source": [
    "Here, you can see that I have tried to access a key value pair from the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "327e427b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total number of parking spaces in 3rd congressional district is :  3266\n"
     ]
    }
   ],
   "source": [
    "# mathematical operation   \n",
    "current = 0\n",
    "countpark = 0\n",
    "while current < 100:\n",
    "    if(building[current]['location']['congressional district'] == '3' ):\n",
    "        countpark += building[current]['data']['parking spaces']\n",
    "    current += 1\n",
    "print(\"Total number of parking spaces in 3rd congressional district is : \",countpark)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a46a06bc",
   "metadata": {},
   "source": [
    "To calculate the number of parking spaces in the first 100 values of the data set where congressional district number is 3, I have included this piece of code performing basic arithmetic operation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c364dbfd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for loop  \n",
    "    \n",
    "for x in range(1,6):\n",
    "    print (\"Index is: \",x,end='')\n",
    "    print (\" The Real estate information is as follows : \" ,building[x])\n",
    "    print(\"-x-\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7ff1cf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "Although we cannot display the entire dataset, I have used for loop iteration to display the first 5 entries in the real estate data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "8063eed5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "103 131\n",
      "I have the largest parking space says  {'city': 'BRIDGEPORT', 'county': 'FAIRFIELD COUNTY', 'line 1': '915 LAFAYETTE BLVD', 'state': 'CT', 'zip': '66044706'}\n"
     ]
    }
   ],
   "source": [
    "# conditional expression \n",
    "c=building[3]['data']['parking spaces']\n",
    "d=building[4]['data']['parking spaces']\n",
    "e=building[3]['location']['address']\n",
    "f=building[4]['location']['address']\n",
    "print(c,d)\n",
    "if(c>d):\n",
    "     print(\"I have the largest parking space says \",e)\n",
    "elif(c==d):\n",
    "    print(\"We have the same parking space\")\n",
    "else:\n",
    "    print(\"I have the largest parking space says \",f)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25cc3882",
   "metadata": {},
   "source": [
    "This conditional expression makes a comparison between two values on the data set and prints the one with the larger parking space."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
