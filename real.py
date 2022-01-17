{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "957bfdf1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ">>> get_building()\n",
      "Time taken: 0.06692959999782033\n",
      "{'data': {'date': '1933.1.1',\n",
      "          'disabilities': {'ADA Accessible': 'Will Conform',\n",
      "                           'ansi usable': '97072'},\n",
      "          'owned or leased': 'OWNED',\n",
      "          'parking spaces': 29,\n",
      "          'status': 'ACTIVE',\n",
      "          'type': 'BUILDING'},\n",
      " 'location': {'address': {'city': 'HARTFORD',\n",
      "                          'county': 'HARTFORD COUNTY',\n",
      "                          'line 1': '135 HIGH ST',\n",
      "                          'state': 'CT',\n",
      "                          'zip': '61031125'},\n",
      "              'congressional district': '1',\n",
      "              'id': 'CT0013',\n",
      "              'region id': '1'}}\n",
      "Present time =  2022-01-16 19:38:21.137887\n",
      "Type of the class :  <class 'list'>\n",
      "Number of rows :  9129\n",
      "Printing keys :  dict_keys(['data', 'location'])\n",
      "Printing values :  dict_values([{'date': '1933.1.1', 'owned or leased': 'OWNED', 'parking spaces': 29, 'status': 'ACTIVE', 'type': 'BUILDING', 'disabilities': {'ADA Accessible': 'Will Conform', 'ansi usable': '97072'}}, {'congressional district': '1', 'id': 'CT0013', 'region id': '1', 'address': {'city': 'HARTFORD', 'county': 'HARTFORD COUNTY', 'line 1': '135 HIGH ST', 'state': 'CT', 'zip': '61031125'}}])\n"
     ]
    }
   ],
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
   "cell_type": "code",
   "execution_count": 94,
   "id": "c980e6a8",
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
   "cell_type": "code",
   "execution_count": 92,
   "id": "d3dea2d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1933.1.1 1\n"
     ]
    }
   ],
   "source": [
    "# commands to read the datafile    \n",
    "a=building[0]['data']['date']\n",
    "b=building[0]['location']['congressional district']\n",
    "print(a,b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "b13048cf",
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
   "cell_type": "code",
   "execution_count": 100,
   "id": "3a4963d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index is:  1 The Real estate information is as follows :  {'data': {'date': '2019.1.1', 'owned or leased': 'OWNED', 'parking spaces': 0, 'status': 'ACTIVE', 'type': 'BUILDING', 'disabilities': {'ADA Accessible': 'Will Conform', 'ansi usable': '67717'}}, 'location': {'congressional district': '3', 'id': 'CT0024', 'region id': '1', 'address': {'city': 'NEW HAVEN', 'county': 'NEW HAVEN COUNTY', 'line 1': '141 CHURCH ST', 'state': 'CT', 'zip': '65102001'}}}\n",
      "-x-\n",
      "Index is:  2 The Real estate information is as follows :  {'data': {'date': '1933.1.1', 'owned or leased': 'LEASED', 'parking spaces': 2, 'status': 'ACTIVE', 'type': 'BUILDING', 'disabilities': {'ADA Accessible': 'Will Conform', 'ansi usable': '7442'}}, 'location': {'congressional district': '5', 'id': 'CT0047', 'region id': '1', 'address': {'city': 'WATERBURY', 'county': 'NEW HAVEN COUNTY', 'line 1': '135 GRAND ST', 'state': 'CT', 'zip': '67029998'}}}\n",
      "-x-\n",
      "Index is:  3 The Real estate information is as follows :  {'data': {'date': '1963.1.1', 'owned or leased': 'OWNED', 'parking spaces': 103, 'status': 'ACTIVE', 'type': 'BUILDING', 'disabilities': {'ADA Accessible': 'Will Conform', 'ansi usable': '203175'}}, 'location': {'congressional district': '1', 'id': 'CT0053', 'region id': '1', 'address': {'city': 'HARTFORD', 'county': 'HARTFORD COUNTY', 'line 1': '450 Main St', 'state': 'CT', 'zip': '61031804'}}}\n",
      "-x-\n",
      "Index is:  4 The Real estate information is as follows :  {'data': {'date': '1967.1.1', 'owned or leased': 'OWNED', 'parking spaces': 131, 'status': 'ACTIVE', 'type': 'BUILDING', 'disabilities': {'ADA Accessible': 'Will Conform', 'ansi usable': '86215'}}, 'location': {'congressional district': '4', 'id': 'CT0059', 'region id': '1', 'address': {'city': 'BRIDGEPORT', 'county': 'FAIRFIELD COUNTY', 'line 1': '915 LAFAYETTE BLVD', 'state': 'CT', 'zip': '66044706'}}}\n",
      "-x-\n",
      "Index is:  5 The Real estate information is as follows :  {'data': {'date': '1969.1.1', 'owned or leased': 'OWNED', 'parking spaces': 5, 'status': 'ACTIVE', 'type': 'BUILDING', 'disabilities': {'ADA Accessible': 'Will Conform', 'ansi usable': '5052'}}, 'location': {'congressional district': '5', 'id': 'CT0060', 'region id': '1', 'address': {'city': 'TORRINGTON', 'county': 'LITCHFIELD COUNTY', 'line 1': '147 Litchfield St', 'state': 'CT', 'zip': '67906407'}}}\n",
      "-x-\n"
     ]
    }
   ],
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
   "execution_count": 102,
   "id": "8d5ed798",
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
   "cell_type": "code",
   "execution_count": null,
   "id": "486a23e7",
   "metadata": {},
   "outputs": [],
   "source": []
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
