{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "d1882547",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "5bf990c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>title</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "      <td>Adventure|Animation|Children|Comedy|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Jumanji (1995)</td>\n",
       "      <td>Adventure|Children|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Grumpier Old Men (1995)</td>\n",
       "      <td>Comedy|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Waiting to Exhale (1995)</td>\n",
       "      <td>Comedy|Drama|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Father of the Bride Part II (1995)</td>\n",
       "      <td>Comedy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>Heat (1995)</td>\n",
       "      <td>Action|Crime|Thriller</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>Sabrina (1995)</td>\n",
       "      <td>Comedy|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>Tom and Huck (1995)</td>\n",
       "      <td>Adventure|Children</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>Sudden Death (1995)</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>GoldenEye (1995)</td>\n",
       "      <td>Action|Adventure|Thriller</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   movieId                               title  \\\n",
       "0        1                    Toy Story (1995)   \n",
       "1        2                      Jumanji (1995)   \n",
       "2        3             Grumpier Old Men (1995)   \n",
       "3        4            Waiting to Exhale (1995)   \n",
       "4        5  Father of the Bride Part II (1995)   \n",
       "5        6                         Heat (1995)   \n",
       "6        7                      Sabrina (1995)   \n",
       "7        8                 Tom and Huck (1995)   \n",
       "8        9                 Sudden Death (1995)   \n",
       "9       10                    GoldenEye (1995)   \n",
       "\n",
       "                                        genres  \n",
       "0  Adventure|Animation|Children|Comedy|Fantasy  \n",
       "1                   Adventure|Children|Fantasy  \n",
       "2                               Comedy|Romance  \n",
       "3                         Comedy|Drama|Romance  \n",
       "4                                       Comedy  \n",
       "5                        Action|Crime|Thriller  \n",
       "6                               Comedy|Romance  \n",
       "7                           Adventure|Children  \n",
       "8                                       Action  \n",
       "9                    Action|Adventure|Thriller  "
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies = pd.read_csv(\"movielens/movies.csv\")\n",
    "movies.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "5631603d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>imdbId</th>\n",
       "      <th>tmdbId</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>114709</td>\n",
       "      <td>862.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>113497</td>\n",
       "      <td>8844.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>113228</td>\n",
       "      <td>15602.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>114885</td>\n",
       "      <td>31357.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>113041</td>\n",
       "      <td>11862.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>113277</td>\n",
       "      <td>949.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>114319</td>\n",
       "      <td>11860.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>112302</td>\n",
       "      <td>45325.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>114576</td>\n",
       "      <td>9091.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>113189</td>\n",
       "      <td>710.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   movieId  imdbId   tmdbId\n",
       "0        1  114709    862.0\n",
       "1        2  113497   8844.0\n",
       "2        3  113228  15602.0\n",
       "3        4  114885  31357.0\n",
       "4        5  113041  11862.0\n",
       "5        6  113277    949.0\n",
       "6        7  114319  11860.0\n",
       "7        8  112302  45325.0\n",
       "8        9  114576   9091.0\n",
       "9       10  113189    710.0"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "links=pd.read_csv('movielens/links.csv')\n",
    "links.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "77b8b938",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>movieId</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964982703</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964981247</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964982224</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964983815</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>50</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964982931</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>70</td>\n",
       "      <td>3.0</td>\n",
       "      <td>964982400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1</td>\n",
       "      <td>101</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964980868</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1</td>\n",
       "      <td>110</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964982176</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1</td>\n",
       "      <td>151</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964984041</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1</td>\n",
       "      <td>157</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964984100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   userId  movieId  rating  timestamp\n",
       "0       1        1     4.0  964982703\n",
       "1       1        3     4.0  964981247\n",
       "2       1        6     4.0  964982224\n",
       "3       1       47     5.0  964983815\n",
       "4       1       50     5.0  964982931\n",
       "5       1       70     3.0  964982400\n",
       "6       1      101     5.0  964980868\n",
       "7       1      110     4.0  964982176\n",
       "8       1      151     5.0  964984041\n",
       "9       1      157     5.0  964984100"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "\n",
    "\n",
    "ratings=pd.read_csv('movielens/ratings.csv')\n",
    "ratings.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "bee8fd99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>movieId</th>\n",
       "      <th>tag</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>60756</td>\n",
       "      <td>funny</td>\n",
       "      <td>1445714994</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>60756</td>\n",
       "      <td>Highly quotable</td>\n",
       "      <td>1445714996</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>60756</td>\n",
       "      <td>will ferrell</td>\n",
       "      <td>1445714992</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>89774</td>\n",
       "      <td>Boxing story</td>\n",
       "      <td>1445715207</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>89774</td>\n",
       "      <td>MMA</td>\n",
       "      <td>1445715200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2</td>\n",
       "      <td>89774</td>\n",
       "      <td>Tom Hardy</td>\n",
       "      <td>1445715205</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2</td>\n",
       "      <td>106782</td>\n",
       "      <td>drugs</td>\n",
       "      <td>1445715054</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2</td>\n",
       "      <td>106782</td>\n",
       "      <td>Leonardo DiCaprio</td>\n",
       "      <td>1445715051</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2</td>\n",
       "      <td>106782</td>\n",
       "      <td>Martin Scorsese</td>\n",
       "      <td>1445715056</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>7</td>\n",
       "      <td>48516</td>\n",
       "      <td>way too long</td>\n",
       "      <td>1169687325</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   userId  movieId                tag   timestamp\n",
       "0       2    60756              funny  1445714994\n",
       "1       2    60756    Highly quotable  1445714996\n",
       "2       2    60756       will ferrell  1445714992\n",
       "3       2    89774       Boxing story  1445715207\n",
       "4       2    89774                MMA  1445715200\n",
       "5       2    89774          Tom Hardy  1445715205\n",
       "6       2   106782              drugs  1445715054\n",
       "7       2   106782  Leonardo DiCaprio  1445715051\n",
       "8       2   106782    Martin Scorsese  1445715056\n",
       "9       7    48516       way too long  1169687325"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tags=pd.read_csv('movielens/tags.csv')\n",
    "tags.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c5c422d",
   "metadata": {},
   "source": [
    "# Exploratory Data Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "8d0826c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape of movies dataframe:  (9742, 3)\n",
      "Shape of ratings dataframe:  (100836, 4)\n",
      "Shape of tags dataframe:  (3683, 4)\n",
      "Shape of links dataframe:  (9742, 3)\n"
     ]
    }
   ],
   "source": [
    "print(\"Shape of movies dataframe: \", movies.shape)\n",
    "print(\"Shape of ratings dataframe: \", ratings.shape)\n",
    "print(\"Shape of tags dataframe: \", tags.shape)\n",
    "print(\"Shape of links dataframe: \", links.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "934a0f9a",
   "metadata": {},
   "source": [
    "## Counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "ae13e580",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of ratings: 100836\n",
      "Number of unique movieId's: 9724\n",
      "Number of unique users: 610\n",
      "Average number of ratings per user: 165.3\n",
      "Average number of ratings per movie: 10.37\n"
     ]
    }
   ],
   "source": [
    "num_ratings = len(ratings)\n",
    "num_movies = ratings['movieId'].nunique()\n",
    "num_users = ratings['userId'].nunique()\n",
    "\n",
    "print(f\"Number of ratings: {num_ratings}\")\n",
    "print(f\"Number of unique movieId's: {num_movies}\")\n",
    "print(f\"Number of unique users: {num_users}\")\n",
    "print(f\"Average number of ratings per user: {round(num_ratings/num_users, 2)}\")\n",
    "print(f\"Average number of ratings per movie: {round(num_ratings/num_movies, 2)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47d8769d",
   "metadata": {},
   "source": [
    "## Movie Ratings Distribution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "1546174d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk0AAAHICAYAAABTb96uAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/NK7nSAAAACXBIWXMAAA9hAAAPYQGoP6dpAABC+ElEQVR4nO3deViVdf7/8dcBPAdNgVzYlNBSMTc0U8LMlRGXLMpKzXHcsmygMhu3yRTbmJw0zVxqGrXNSa3RUhuMULEMs1BySRk1XBpFLRNcChDu3x/+uL8eWbxF9Bzx+biu+7o89/0+9/3+nPscfXnf97mPzTAMQwAAACiTh6sbAAAAuBYQmgAAACwgNAEAAFhAaAIAALCA0AQAAGABoQkAAMACQhMAAIAFhCYAAAALCE0AAAAWEJqAcli3bp1sNpvi4+Ndsv369eurfv36TvPi4+Nls9m0bt06l/S0b98+2Ww2DRkyxCXbrwj5+fmKj49Xo0aN5HA4ZLPZtHz5cle3dVmGDBkim82mffv2ubqVK8LVn0VcXwhNuG4V/SN//lStWjUFBwerW7dumjRpkvbu3XtFtt25c2fZbLYrsu4rqaSwVplMmzZNU6ZMUXBwsP7yl79o8uTJatKkSZnPqV+/vvn+2b59e4k1BQUFqlu3rllXmQLM+eO32Wzy9PRUrVq11K1bNy1durRCtmGz2dS5c+cKWRdwObxc3QDgarfccov++Mc/SpJyc3N19OhRbdq0SS+88IJefvlljR07Vi+99JJTyGnXrp127typ2rVru6Tn5ORkl2y3LHXr1tXOnTvl6+vr6lbKbeXKlapevbqSkpJkt9stP8/D49z/P+fPn6/p06cXW/6f//xHhw4dkpeXl86ePVth/VqRkJCg8ePHq27duldsG56enpo4caKkc0fr9uzZo2XLlmnNmjV6+eWXNWHChCu2bVd/FnF9ITThutewYcMSD+1/9dVXGjRokBISEuTp6akXXnjBXFatWrWLHoG4km655RaXbbs0VapUcelrUhEOHTqkWrVqXVJgks6NvWPHjnr//ff1yiuvqEqVKk7L58+fL19fX4WHh2v9+vUV2fJFBQUFKSgo6Ipuw8vLq9hnaMOGDerYsaNeeOEFPfXUU6pWrdoV2barP4u4vnB6DihFhw4dlJiYKIfDoalTp+rgwYPmstKuo9i9e7eGDh2qBg0ayOFwqGbNmgoPD9eoUaNkGIakc6caUlJSzD8XTUXXAp1/bdDOnTt13333qVatWk6ndS52muyf//ynWrRoIW9vb9WtW1dPP/20Tp486VRT1rUgF16fVPR4//792r9/v1PfRc8v65qm/fv3a/jw4apbt67sdrvq1aun4cOH68CBA8Vqi05dFl1fVL9+fTkcDjVu3Fhz5swpdcylWbBggSIiIlS9enVVr15dERERWrhwoVNN0fVgmZmZTuO7lFORw4YN07Fjx7RixQqn+ceOHdPKlSs1YMAAVa1a9bL6/PLLL2Wz2TRs2LAS13H06FFVqVJFd955pzmvrGua1q9frz59+qh27dpyOBxq1KiRJk6cqDNnzlged2nuvPNONWnSRL/99pt++OEHp2Vr167VsGHDFBYWZo739ttv11tvveVUV/QelaSUlBSn913Ra1Pa+7joM3Lq1Ck99dRTCg4OlsPhUMuWLfXRRx+V2PO+ffvUr18/1axZU9WrV1enTp20fv36Uq8X/Pjjj9WpUyf5+/vL29tbwcHBioqK0scff1z+Fw5ujSNNQBnCwsL00EMP6b333tPy5cv1xBNPlFp76NAhtWvXTqdPn1bv3r3Vr18/nT59Wrt379acOXP06quvysvLS5MnT9bChQu1f/9+TZ482Xx+q1atnNa3Z88e3XHHHWrRooWGDBmiX375xdIRkOnTpys5OVn9+vVT79699cUXX2jGjBnauHGj1q9fX+woiBV+fn6aPHmyZsyYIUkaNWqUuexi15r897//VYcOHXTs2DH16dNHzZo10/bt2zV//nytWLFCX331lRo3blzseQMGDNCmTZvUs2dPeXp6asmSJYqNjVWVKlU0YsQIS30/+eSTmjVrlurWravhw4dLOvcP3dChQ7VlyxbNnDnTaQwXjs/Pz8/SdiTpvvvu04033qgFCxbo/vvvN+e/9957ys/P17Bhw/Tcc89dVp8dOnRQ/fr19fHHH2vOnDny9vZ2Ws+//vUvnT17VoMGDbpov3PnzlVsbKz8/PzUp08f+fv767vvvtNLL72ktWvXau3atZd8xK00Xl7O/9S88sor5vv7vvvu04kTJ5SYmKjHHntMGRkZmjZtmqRzwWfy5MmaMmWKQkNDnQL5hZ+XkuTn56t79+769ddf1bdvX505c0YffvihHnroISUmJqp79+5m7f/+9z+1b99ehw8fVo8ePdS6dWtlZGToD3/4g7p27Vps3XPnztWf//xnBQUFmf+xycrK0qZNm7Rs2TL17du3fC8W3JsBXKcyMzMNSUZ0dHSZdf/85z8NScagQYPMeWvXrjUkGZMnTzbnvf7664YkY8aMGcXW8csvvzg97tSpk1Hax6+oL0nGpEmTSqwJDQ01QkNDneZNnjzZkGTY7Xbj+++/N+cXFhYaDz/8sCHJePXVV8scw4U9DB48+KLbvdhzunTpYkgy3nzzTaf5s2fPNiQZXbt2dZpf9NpEREQY2dnZ5vxdu3YZXl5eRlhYWInbv1BKSoohybj11luNEydOmPOPHz9uNG7c2JBkrF+/3vL4ShMaGmo4HA7DMAwjLi7O8PLyMg4fPmwub9asmdGiRQvDMAwjOjrakGRkZmaWu8+JEycakozFixcX66VNmzaG3W53er8NHjy42DZ37NhheHl5GeHh4cbPP//stI6EhIRi7xWr4z/fV199ZXh4eBi1atUyfvvtN6dlP/74Y7H6/Px84w9/+IPh6elp7N+/32mZJKNTp04lbr+093FoaKghybj33nuN3Nxcc/4XX3xR4uf+j3/8oyHJeOmll5zmF33+JRlr16415992222G3W43jhw5UqynC19TVB6cngMuIjg4WJL0888/W6ov6RRMzZo1L3m7gYGBevbZZy/5eX/605/UsmVL87HNZtPLL78sT0/PYqd7rrQDBw5o7dq1atq0abGjQyNHjlSTJk20Zs0ap1OfRRISEuTj42M+DgsL05133qmMjIxipxpL8s4770g6d+rt/IvTb7zxRvMIX0W/HsOGDdPZs2fNbX/zzTfasWNHqafTytNn0VGk999/32k9O3fuVFpamnr16nXR99ubb76ps2fPatasWapVq5bTsrFjx6pOnTr617/+dZHR/p+zZ88qPj5e8fHxevbZZ9WvXz916dJFHh4eJR4Ra9CgQbF1eHl5aeTIkSooKNDatWstb/tiXnvtNacjZt26dVNoaKi+/fZbc15ubq6WLl0qf39/PfPMM07PHzp0qMLCwkpcd5UqVUo8cnvha4rKg9NzQAXp06ePJkyYoNjYWCUnJ6tHjx7q1KmTbr755nKtLzw8vFynR+66665i80JDQxUSEqIdO3YoLy+vwk67XEx6erokqVOnTsVuseDh4aGOHTtq165dSk9PV0hIiNPyNm3aFFtfvXr1JEknTpxQjRo1ytz2li1bJJV8+rBLly5O/VWU1q1bq1WrVlqwYIHGjRun+fPny263m9/OrIg+GzdurHbt2ikxMVE///yz+a2xohBl5dTcxo0bJUmrV68u8ZuYVapU0a5duy66niIFBQWaMmWK0zwvLy8tXbpUMTExxepPnjypV199VcuXL9fevXt1+vRpp+WHDh2yvO2y+Pn5lRjQ6tWrp9TUVPNxRkaGcnNzdfvtt8vhcDjV2mw2tW/fXhkZGU7z+/fvr7Fjx6p58+Z6+OGH1aVLF3Xo0MEp6KPyITQBF1H0F3idOnXKrKtfv742btyo+Ph4ffbZZ1qyZIkkqUmTJnr++ef14IMPXtJ2AwICytVvac8LCAjQvn37dPLkyav2P+GcnJwyeyr6VldR3flK+sen6NqYgoICS9v28PAocb8FBATIZrOVuN3LNWzYMD355JP64osv9OGHH5oXWldkn4MGDdKmTZu0ePFixcbGyjAMffDBB7rxxhvVu3fvi/Z4/PhxSdJLL710iaMrmcPh0O+//y5JOnXqlNasWaNhw4Zp0KBB+uqrrxQeHm7W5uXlqXPnztq8ebNat26tQYMGqVatWvLy8tK+ffv0zjvvKDc3t0L6Ku32F15eXiosLDQfF72+/v7+JdaX9P79y1/+olq1amnu3LmaNm2aec1i79699dprr5UY1nDt4/QccBFF35hp27btRWubN2+ujz76SMePH1dqaqomTZqkrKws9evXTxs2bLik7Zb35pdHjhwpdb7NZjOP0BTdW6ik+wZlZ2eXa9sXKgo+pfWUlZXlVFeRfHx8VFhYqGPHjhVbdvToURmGcUW2O3DgQDkcDg0ZMkQ5OTnmhd0V2Wf//v1VpUoV8+jS+vXrtX//fj300EPFjpSUtk3pXFgwDKPUqTyqV6+ue+65R4sXL9apU6c0dOhQp3V98skn2rx5s4YPH67Nmzdr7ty5evHFFxUfH68ePXqUa5uXq+j1OHr0aInLS3r/Fn2L8dtvv9WxY8e0bNky3X///frkk0909913Wwr2uPYQmoAy/Pe//9WSJUvkcDh03333WX5elSpVdMcdd2jKlCl6/fXXZRiGVq5caS739PSUZO2IyaX68ssvi83bv3+/Dh48qGbNmpmn5m688UZJ5741dKGiU0YX8vT0vKSei77htH79+mL/CBuGYd6zyMo3oS5V69atJanEn5UpmncltluzZk3FxMTof//7n+rWravo6Ogy68vTZ+3atdWjRw9t3LhRe/bsMcNTWacBzxcRESHp/07TXQndunVTTEyMtmzZ4nR9VNFd9u+9995izynpvSudC/hXMoSEhYXJ4XAoLS2t2FEuwzCcTuWVpFatWoqJidHixYvVtWtX/fDDD9qzZ88V6xeuQ2gCSrFhwwZFR0crNzfX0h2V09LSSjzdU/S/1PMvhi26ULekC6Av17vvvqutW7eajw3D0F//+lcVFBQ4fWU7LCxMNWrU0Keffmqerinq98UXXyxx3TVr1tTPP/9snoq5mJtuukldunTRjh07NH/+fKdlb731lnbu3KmuXbsWu56pIgwePFiSNGXKFKf9kp2dbV5/U1RT0f72t79p2bJlWr58uXlEr6L7LLp26e2339bSpUvVoEEDp/szleXPf/6zvLy89MQTT5R4r6wTJ06UGpwvRdH9jaZMmWKGntDQUEnnbh57vpSUFP3jH/8ocT01a9bUTz/9dNn9lMbhcOiBBx7QkSNHzNtOFHn33XdLvL5r3bp1xf4jkJ+fb36WLrz4HZUD1zThurdnzx7zxnh5eXnmz6hs27bN/HmI8++nVJr33ntPb775pjp27KhbbrlFPj4++uGHH/TZZ5+pZs2aGjp0qFnbtWtXffTRR+rbt6969uwpb29vhYeHq0+fPpc9nujoaEVGRqp///6qU6eOkpOT9d133+mOO+5wus+U3W7XE088oZdfflm33Xab7r33Xp08eVIrVqxQp06dSvzdva5du+q7775Tz549ddddd8lut6tjx47q2LFjqf3MnTtXHTp00IgRI7RixQo1bdpUO3bs0Keffqo6depo7ty5lz3mknTs2FFPPPGEZs2apebNm6tv374yDEMff/yxfvrpJz355JNl9n05LuU3+srbZ58+feTr66vp06crPz9fTz75pOVTus2bN9ecOXP0+OOPKywsTL169dItt9yikydP6scff1RKSoqGDBmiefPmXcqwiwkPD9d9992nf//733r//fc1ePBg9enTR/Xr19fUqVO1fft2NW/eXBkZGVq5cqXuu+++Em882bVrVy1ZskQxMTFq3bq1PD09dc899zh9S/RyJSQk6IsvvtD48eOVkpJi3qdp5cqV6tGjhxITE50CcExM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1yUdaQoNDZUkFRYWXpFmLtSjRw/df//9atCggfbu3au//vWv6tmzp1JTU+Xp6amsrCz5+/s7PcfLy0s1a9Y0Tx1mZWWpQYMGTjUBAQHmshtvvFFZWVnmvPNrzj/9eKGEhARNmTKlIoYJAACuAZcUms63e/durV27VkePHi0WoiZNmnTZjUlS//79zT+3aNFCLVu21C233KJ169apW7duFbKN8powYYJGjx5tPs7JyVFISIgLOwIAAFdSuULTP/7xDz3++OOqXbu2AgMDZbPZzGU2m63CQtOFbr75ZtWuXVt79uxRt27dFBgYqKNHjzrVnD17VsePHzevgwoMDNSRI0ecaooeX6ymtGuppHPXWl14UToAAKi8ynXLgRdffFEvvfSSsrKylJ6eri1btpjT5s2bK7pH008//aRffvlFQUFBkqTIyEidOHFCaWlpZs2aNWtUWFioiIgIs2b9+vXKz883a5KSkhQWFqYbb7zRrElOTnbaVlJSkiIjI6/YWAAAwLWlXKHp119/1YMPPnjZGz916pTS09OVnp4u6dyF5unp6Tpw4IBOnTqlMWPGaOPGjdq3b5+Sk5N17733qmHDhoqOjpYk3XrrrerRo4dGjBihTZs2acOGDYqLi1P//v0VHBwsSXr44Ydlt9s1fPhw7dixQ4sXL9bMmTOdTq099dRTSkxM1LRp07Rr1y7Fx8fru+++U1xc3GWPEQAAVA7lCk0PPvigPv/888ve+HfffafWrVurdevWkqTRo0erdevWmjRpkjw9PbV161bdc889aty4sYYPH642bdroyy+/dDot9sEHH6hJkybq1q2bevXqpQ4dOuitt94yl/v6+urzzz9XZmam2rRpo2eeeUaTJk0ybzcgSe3bt9eiRYv01ltvKTw8XB999JGWL1/OPZoAAICpXNc0NWzYUM8995w2btyoFi1aqEqVKk7Ln3zySUvr6dy5swzDKHX56tWrL7qOmjVrmjeyLE3Lli0veqfyBx98sEKOngEAgMqpXKHprbfeUvXq1ZWSkqKUlBSnZTabzXJoAgAAuFaUKzRlZmZWdB8AAABurVzXNAEAAFxvynWk6WI/lTJ//vxyNQMAAOCuyhWain6zrUh+fr62b9+uEydOlPhDvgAAANe6coWmZcuWFZtXWFioxx9/XLfccstlNwUAAOBuKuyaJg8PD40ePVqvvfZa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bfw85RmDO34uhg0bZoSGhhp2u92oU6eO0a1bNzNoGIb774cilzoOd9wXJbkwbFwr++NCFxuHu+2Pfv36GUFBQYbdbjfq1q1r9OvXz9izZ4+53B33g80wDOPqHdcCAAC4NnFNEwAAgAWEJgAAAAsITQAAABYQmgAAACwgNAEAAFhAaAIAALCA0AQAAGABoQkALKhfv75mzJjh6jYAuBChCQDOs3DhQvn5+RWb/+233+rRRx+9+g0BcBterm4AAK6WvLw82e32cj23Tp06FdwNgGsNR5oAVFqdO3dWXFycRo0apdq1ays6OlrTp09XixYtdMMNNygkJER//vOfderUKUnSunXrNHToUGVnZ8tms8lmsyk+Pl5S8dNzNptNb7/9tu677z5Vq1ZNjRo10qeffuq0/U8//VSNGjWSt7e3unTponfeeUc2m00nTpy4Sq8AgIpEaAJQqb3zzjuy2+3asGGD5s2bJw8PD73++uvasWOH3nnnHa1Zs0Zjx46VJLVv314zZsyQj4+PDh8+rMOHD+svf/lLqeueMmWKHnroIW3dulW9evXSwIEDdfz4cUlSZmamHnjgAcXExOj777/XY489pmefffaqjBnAlcHpOQCVWqNGjTR16lTzcVhYmPnn+vXr68UXX9TIkSM1Z84c2e12+fr6ymazKTAw8KLrHjJkiAYMGCBJevnll/X6669r06ZN6tGjh958802FhYXp73//u7nd7du366WXXqrgEQK4WghNACq1Nm3aOD3+4osvlJCQoF27diknJ0dnz57V77//rjNnzqhatWqXtO6WLVuaf77hhhvk4+Ojo0ePSpIyMjLUtm1bp/p27dqVcxQA3AGn5wBUajfccIP553379unuu+9Wy5Yt9fHHHystLU2zZ8+WdO4i8UtVpUoVp8c2m02FhYWX1zAAt8WRJgDXjbS0NBUWFmratGny8Dj3f8YlS5Y41djtdhUUFFz2tsLCwvTZZ585zfv2228ve70AXIcjTQCuGw0bNlR+fr5mzZqlH3/8Ue+9957mzZvnVFO/fn2dOnVKycnJ+vnnn3XmzJlybeuxxx7Trl27NG7cOP33v//VkiVLtHDhQknnjkgBuPYQmgBcN8LDwzV9+nS98sorat68uT744AMlJCQ41bRv314jR45Uv379VKdOHaeLyC9FgwYN9NFHH+nf//63WrZsqblz55rfnnM4HJc9FgBXn80wDMPVTQDA9eCll17SvHnzdPDgQVe3AqAcuKYJAK6QOXPmqG3btqpVq5Y2bNigv//974qLi3N1WwDKidAEAFfI7t279eKLL+r48eO66aab9Mwzz2jChAmubgtAOXF6DgAAwAIuBAcAALCA0AQAAGABoQkAAMACQhMAAIAFhCYAAAALCE0AAAAWEJoAAAAsIDQBAABYQGgCAACw4P8ByyseOTLJ/yMAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "sns.countplot(x='rating', data=ratings)\n",
    "plt.title(\"Distribution of Movie Ratings\", fontsize=14)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b36be88e",
   "metadata": {},
   "source": [
    "### Mean Rating Per User"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "f6bf3cd8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean rating per user: 3.66\n"
     ]
    }
   ],
   "source": [
    "mean_ratings = ratings.groupby('userId')['rating'].mean()\n",
    "print(f\"Mean rating per user: {round(mean_ratings.mean(), 2)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42322cc3",
   "metadata": {},
   "source": [
    "### Most Rated Movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "ca96caf1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Forrest Gump (1994)                          329\n",
       "Shawshank Redemption, The (1994)             317\n",
       "Pulp Fiction (1994)                          307\n",
       "Silence of the Lambs, The (1991)             279\n",
       "Matrix, The (1999)                           278\n",
       "Star Wars: Episode IV - A New Hope (1977)    251\n",
       "Jurassic Park (1993)                         238\n",
       "Braveheart (1995)                            237\n",
       "Terminator 2: Judgment Day (1991)            224\n",
       "Schindler's List (1993)                      220\n",
       "Name: title, dtype: int64"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_ratings = ratings.merge(movies, on='movieId')\n",
    "movie_ratings['title'].value_counts()[0:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7355b218",
   "metadata": {},
   "source": [
    "### Top and Least rated movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "53206e2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>title</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2689</th>\n",
       "      <td>3604</td>\n",
       "      <td>Gypsy (1962)</td>\n",
       "      <td>Musical</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      movieId         title   genres\n",
       "2689     3604  Gypsy (1962)  Musical"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean_ratings = ratings.groupby('movieId')[['rating']].mean()\n",
    "lowest_rated = mean_ratings['rating'].idxmin()\n",
    "movies[movies['movieId']==lowest_rated]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "d6c8e472",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>title</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>53</td>\n",
       "      <td>Lamerica (1994)</td>\n",
       "      <td>Adventure|Drama</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    movieId            title           genres\n",
       "48       53  Lamerica (1994)  Adventure|Drama"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "highest_rated = mean_ratings['rating'].idxmax()\n",
    "movies[movies['movieId'] == highest_rated]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "6f578d4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>movieId</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>13368</th>\n",
       "      <td>85</td>\n",
       "      <td>53</td>\n",
       "      <td>5.0</td>\n",
       "      <td>889468268</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96115</th>\n",
       "      <td>603</td>\n",
       "      <td>53</td>\n",
       "      <td>5.0</td>\n",
       "      <td>963180003</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       userId  movieId  rating  timestamp\n",
       "13368      85       53     5.0  889468268\n",
       "96115     603       53     5.0  963180003"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings[ratings['movieId']==highest_rated]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3498bc0",
   "metadata": {},
   "source": [
    "### Bayesian Average and Why it is important here?\n"
   ]
  },
  {
   "attachments": {
    "Screenshot%202024-10-09%20at%2000.41.08.png": {
     "image/png": "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+xrTtHdD3YcoIXC9VmrlypUN0ek9s2uzGOdPeMITGsaVOjNyXYd73/vezROf+MT23beL7e8vf/nL7auNCGoREKIWNt988/oy68XnDXlMH3300a0H3juNhTDz4F7pSldqv1uxYsXcfNfWc2Xuii7jCcaNj3G/LWOVcuoQCIENkECE7gbYaalyCAyFgAmLib8EVGecccYazSI8hWIuV2IoYYYS9nznO99pr20d8IMe9KBWaKxRmc4Xkgv94he/aENRL3e5yy1LOKwMr9Z48s55p+9mm202s7dPPU3InYvXyetPNtlkk7HrCAkxwownVFg50WUyL6x20rH61HHeMerPZ9cVCu5411/boZ3WfBOR61LoGj7C8q2ZZVjpW+OJk9cECTnGeTFFQre73e1u7WuzsP70pz+92vugjQPXLn/612fb8tk6+BJCbeyUflQffSfUetbQfuPA+4WNK3/GmPpZmuCPUYsxa9x5jS1/OE1TCuPu/tOcZ9I+X/va1xpGBfem9fx3vOMd24Ri09Srbx/nkUQMF/esew4LvCUTMx78jTOAqPO43+vrYmNffz53GdX7ls99TKY5tu+4ck5bY7I8p7TfWHFeY1D7jQ/r142RP/7xj+0z0dhZsWBUmLa99fXyOQRCYOMhEKG78fR1WhoC6x0BkxYe209+8pNreLlM7g5eCGfefffd2wnOclS+9uiaTL3iFa9obnvb266a5I+75vHHH9+86EUvagUFgayexOhSTbxM9r7xjW+0ryyx3XvvvVsRPq13zuSSwFNPgp5gNjm85jWv2cgsbSuTdS06TbYJpdNPP72RXdYxvKH2IX623HLLdh2p8Fr1qI/FipBxjFfcEHVe4eQdr4SRY6985Ss32267betpXIxoH9cf436TpInQ9U7bdeXRLfX78Ic/3EYw4KSPusUYkjlZPY3JxZRnPvOZq4wwjEj6WSFaJUvi7dVX+ttWOG75853jeYNxs75YaD+jjqLfjZ8b3OAGrcCbNN6JmN/97netMUk2de8XNjaKAcS6Vt71G97whs0tbnGLZrvttmvHWt95jSVjugi+vn0KU0JJe415hrJ6X8m6MOiu1S7H2hJc/ryHeJz4bqHM8R+8tQmbL33pSy0nvBTPQPedsHZh6Le5zW3a+6ivPuqsn2wJxLq9pXp+81fYYO/87ldCktgddxwx6thtttmmPSWD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SkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAIBhW4WZtkxSkACEpCABCQgAQlIQAISyBABhW6GJtuhSkACEpCABCQgAQlIQAISyAKB/wXozSMBPRKvpgAAAABJRU5ErkJggg=="
    }
   },
   "cell_type": "markdown",
   "id": "1dadc62a",
   "metadata": {},
   "source": [
    "Movies with perfect ratings but with very less ratings may affect the reliability of our engine. So to avoid these problems, we use Bayesian Average. \n",
    "\n",
    "It is calculated as follows:\n",
    "![Screenshot%202024-10-09%20at%2000.41.08.png](attachment:Screenshot%202024-10-09%20at%2000.41.08.png)\n",
    "\n",
    "Here C represents our confidence, m represents our prior, and N is the total number of reviews for movie . In this case, our prior will be the average mean rating across all movies. By defintion, C represents \"the typical data set size\". Let's make  be the average number of ratings for a given movie."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "dbab32e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>movieId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>215</td>\n",
       "      <td>3.920930</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>110</td>\n",
       "      <td>3.431818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>52</td>\n",
       "      <td>3.259615</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7</td>\n",
       "      <td>2.357143</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>49</td>\n",
       "      <td>3.071429</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         count      mean\n",
       "movieId                 \n",
       "1          215  3.920930\n",
       "2          110  3.431818\n",
       "3           52  3.259615\n",
       "4            7  2.357143\n",
       "5           49  3.071429"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_stats = ratings.groupby('movieId')['rating'].agg(['count', 'mean'])\n",
    "movie_stats.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "566183c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average number of ratings for a given movie: 10.37\n",
      "Average rating for a given movie: 3.26\n"
     ]
    }
   ],
   "source": [
    "C = movie_stats['count'].mean()\n",
    "m = movie_stats['mean'].mean()\n",
    "\n",
    "print(f\"Average number of ratings for a given movie: {C:.2f}\")\n",
    "print(f\"Average rating for a given movie: {m:.2f}\")\n",
    "\n",
    "def bayesian_avg(ratings):\n",
    "    bayesian_avg = (C*m+ratings.sum())/(C+ratings.count())\n",
    "    return round(bayesian_avg, 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df835cf0",
   "metadata": {},
   "source": [
    "#### Testing the above function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "86f94c5c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.543"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lamerica = pd.Series([5, 5])\n",
    "bayesian_avg(lamerica)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "2595554e",
   "metadata": {},
   "outputs": [],
   "source": [
    "## For others\n",
    "bayesian_avg_ratings = ratings.groupby('movieId')['rating'].agg(bayesian_avg).reset_index()\n",
    "bayesian_avg_ratings.columns = ['movieId', 'bayesian_avg']\n",
    "movie_stats = movie_stats.merge(bayesian_avg_ratings, on='movieId')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "60b60f4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>bayesian_avg</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>277</th>\n",
       "      <td>318</td>\n",
       "      <td>317</td>\n",
       "      <td>4.429022</td>\n",
       "      <td>4.392</td>\n",
       "      <td>Shawshank Redemption, The (1994)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>659</th>\n",
       "      <td>858</td>\n",
       "      <td>192</td>\n",
       "      <td>4.289062</td>\n",
       "      <td>4.236</td>\n",
       "      <td>Godfather, The (1972)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2224</th>\n",
       "      <td>2959</td>\n",
       "      <td>218</td>\n",
       "      <td>4.272936</td>\n",
       "      <td>4.227</td>\n",
       "      <td>Fight Club (1999)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>224</th>\n",
       "      <td>260</td>\n",
       "      <td>251</td>\n",
       "      <td>4.231076</td>\n",
       "      <td>4.193</td>\n",
       "      <td>Star Wars: Episode IV - A New Hope (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>50</td>\n",
       "      <td>204</td>\n",
       "      <td>4.237745</td>\n",
       "      <td>4.191</td>\n",
       "      <td>Usual Suspects, The (1995)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      movieId  count      mean  bayesian_avg  \\\n",
       "277       318    317  4.429022         4.392   \n",
       "659       858    192  4.289062         4.236   \n",
       "2224     2959    218  4.272936         4.227   \n",
       "224       260    251  4.231076         4.193   \n",
       "46         50    204  4.237745         4.191   \n",
       "\n",
       "                                          title  \n",
       "277            Shawshank Redemption, The (1994)  \n",
       "659                       Godfather, The (1972)  \n",
       "2224                          Fight Club (1999)  \n",
       "224   Star Wars: Episode IV - A New Hope (1977)  \n",
       "46                   Usual Suspects, The (1995)  "
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_stats = movie_stats.merge(movies[['movieId', 'title']])\n",
    "movie_stats.sort_values('bayesian_avg', ascending=False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "008510eb",
   "metadata": {},
   "source": [
    "Here We can see that Popular and most Critically acclaimed movies are the top rated movies in this dataset. Also, the number of ratings on these movies is high. So it makes more sense than Lamerica being the highest rated movie."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "136586bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>bayesian_avg</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1172</th>\n",
       "      <td>1556</td>\n",
       "      <td>19</td>\n",
       "      <td>1.605263</td>\n",
       "      <td>2.190</td>\n",
       "      <td>Speed 2: Cruise Control (1997)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2679</th>\n",
       "      <td>3593</td>\n",
       "      <td>19</td>\n",
       "      <td>1.657895</td>\n",
       "      <td>2.224</td>\n",
       "      <td>Battlefield Earth (2000)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1372</th>\n",
       "      <td>1882</td>\n",
       "      <td>33</td>\n",
       "      <td>1.954545</td>\n",
       "      <td>2.267</td>\n",
       "      <td>Godzilla (1998)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1144</th>\n",
       "      <td>1499</td>\n",
       "      <td>27</td>\n",
       "      <td>1.925926</td>\n",
       "      <td>2.297</td>\n",
       "      <td>Anaconda (1997)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1988</th>\n",
       "      <td>2643</td>\n",
       "      <td>16</td>\n",
       "      <td>1.687500</td>\n",
       "      <td>2.307</td>\n",
       "      <td>Superman IV: The Quest for Peace (1987)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      movieId  count      mean  bayesian_avg  \\\n",
       "1172     1556     19  1.605263         2.190   \n",
       "2679     3593     19  1.657895         2.224   \n",
       "1372     1882     33  1.954545         2.267   \n",
       "1144     1499     27  1.925926         2.297   \n",
       "1988     2643     16  1.687500         2.307   \n",
       "\n",
       "                                        title  \n",
       "1172           Speed 2: Cruise Control (1997)  \n",
       "2679                 Battlefield Earth (2000)  \n",
       "1372                          Godzilla (1998)  \n",
       "1144                          Anaconda (1997)  \n",
       "1988  Superman IV: The Quest for Peace (1987)  "
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_stats.sort_values('bayesian_avg', ascending=True).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef6d729b",
   "metadata": {},
   "source": [
    "We do the same for lowest rated movies."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dcf56e92",
   "metadata": {},
   "source": [
    "### Movies dataframe\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "2ade72a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>title</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "      <td>Adventure|Animation|Children|Comedy|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Jumanji (1995)</td>\n",
       "      <td>Adventure|Children|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Grumpier Old Men (1995)</td>\n",
       "      <td>Comedy|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Waiting to Exhale (1995)</td>\n",
       "      <td>Comedy|Drama|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Father of the Bride Part II (1995)</td>\n",
       "      <td>Comedy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9737</th>\n",
       "      <td>193581</td>\n",
       "      <td>Black Butler: Book of the Atlantic (2017)</td>\n",
       "      <td>Action|Animation|Comedy|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9738</th>\n",
       "      <td>193583</td>\n",
       "      <td>No Game No Life: Zero (2017)</td>\n",
       "      <td>Animation|Comedy|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9739</th>\n",
       "      <td>193585</td>\n",
       "      <td>Flint (2017)</td>\n",
       "      <td>Drama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9740</th>\n",
       "      <td>193587</td>\n",
       "      <td>Bungo Stray Dogs: Dead Apple (2018)</td>\n",
       "      <td>Action|Animation</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9741</th>\n",
       "      <td>193609</td>\n",
       "      <td>Andrew Dice Clay: Dice Rules (1991)</td>\n",
       "      <td>Comedy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>9742 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      movieId                                      title  \\\n",
       "0           1                           Toy Story (1995)   \n",
       "1           2                             Jumanji (1995)   \n",
       "2           3                    Grumpier Old Men (1995)   \n",
       "3           4                   Waiting to Exhale (1995)   \n",
       "4           5         Father of the Bride Part II (1995)   \n",
       "...       ...                                        ...   \n",
       "9737   193581  Black Butler: Book of the Atlantic (2017)   \n",
       "9738   193583               No Game No Life: Zero (2017)   \n",
       "9739   193585                               Flint (2017)   \n",
       "9740   193587        Bungo Stray Dogs: Dead Apple (2018)   \n",
       "9741   193609        Andrew Dice Clay: Dice Rules (1991)   \n",
       "\n",
       "                                           genres  \n",
       "0     Adventure|Animation|Children|Comedy|Fantasy  \n",
       "1                      Adventure|Children|Fantasy  \n",
       "2                                  Comedy|Romance  \n",
       "3                            Comedy|Drama|Romance  \n",
       "4                                          Comedy  \n",
       "...                                           ...  \n",
       "9737              Action|Animation|Comedy|Fantasy  \n",
       "9738                     Animation|Comedy|Fantasy  \n",
       "9739                                        Drama  \n",
       "9740                             Action|Animation  \n",
       "9741                                       Comedy  \n",
       "\n",
       "[9742 rows x 3 columns]"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1db275dc",
   "metadata": {},
   "source": [
    "#### 1. title has date in it\n",
    "#### 2. genre has | separating each item.\n",
    "\n",
    "## Do:\n",
    "\n",
    "#### 1. Extract date and create a new column \n",
    "#### 2. Remove the | seperator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "11365398",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movieId</th>\n",
       "      <th>title</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "      <td>[Adventure, Animation, Children, Comedy, Fantasy]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Jumanji (1995)</td>\n",
       "      <td>[Adventure, Children, Fantasy]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Grumpier Old Men (1995)</td>\n",
       "      <td>[Comedy, Romance]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Waiting to Exhale (1995)</td>\n",
       "      <td>[Comedy, Drama, Romance]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Father of the Bride Part II (1995)</td>\n",
       "      <td>[Comedy]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   movieId                               title  \\\n",
       "0        1                    Toy Story (1995)   \n",
       "1        2                      Jumanji (1995)   \n",
       "2        3             Grumpier Old Men (1995)   \n",
       "3        4            Waiting to Exhale (1995)   \n",
       "4        5  Father of the Bride Part II (1995)   \n",
       "\n",
       "                                              genres  \n",
       "0  [Adventure, Animation, Children, Comedy, Fantasy]  \n",
       "1                     [Adventure, Children, Fantasy]  \n",
       "2                                  [Comedy, Romance]  \n",
       "3                           [Comedy, Drama, Romance]  \n",
       "4                                           [Comedy]  "
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies['genres'] = movies['genres'].apply(lambda x: x.split(\"|\"))\n",
    "movies.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97b6beca",
   "metadata": {},
   "source": [
    "### Number of movies genres (frequency)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "dc392c14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 20 genres.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Counter({'Adventure': 1263,\n",
       "         'Animation': 611,\n",
       "         'Children': 664,\n",
       "         'Comedy': 3756,\n",
       "         'Fantasy': 779,\n",
       "         'Romance': 1596,\n",
       "         'Drama': 4361,\n",
       "         'Action': 1828,\n",
       "         'Crime': 1199,\n",
       "         'Thriller': 1894,\n",
       "         'Horror': 978,\n",
       "         'Mystery': 573,\n",
       "         'Sci-Fi': 980,\n",
       "         'War': 382,\n",
       "         'Musical': 334,\n",
       "         'Documentary': 440,\n",
       "         'IMAX': 158,\n",
       "         'Western': 167,\n",
       "         'Film-Noir': 87,\n",
       "         '(no genres listed)': 34})"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from collections import Counter\n",
    "\n",
    "genre_frequency = Counter(g for genres in movies['genres'] for g in genres)\n",
    "\n",
    "print(f\"There are {len(genre_frequency)} genres.\")\n",
    "\n",
    "genre_frequency"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "2acce68b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The 5 most common genres: \n",
      " [('Drama', 4361), ('Comedy', 3756), ('Thriller', 1894), ('Action', 1828), ('Romance', 1596)]\n"
     ]
    }
   ],
   "source": [
    "print(\"The 5 most common genres: \\n\", genre_frequency.most_common(5))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f2da6d5",
   "metadata": {},
   "source": [
    "#### Plotting "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "7786a36c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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RERElB8KzGX3lLduruwsa70aw/8naz0iIqK8xCNEREREpHgMRERERKR4DERERESkeAxEREREpHgcVE1aE7jOVdZ6rQZzIk0iItIOHiEiIiIixWMgIiIiIsVjICIiIiLFYyAiIiIixWMgIiIiIsVjICIiIiLFYyAiIiIixWMgIiIiIsVjICIiIiLFYyAiIiIixWMgIiIiIsVjICIiIiLFYyAiIiIixWMgIiIiIsVjICIiIiLFYyAiIiIixWMgIiIiIsVjICIiIiLF08vvDhBpYpdPO1nr9Rh4WNZ6RERUOPAIERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpnl5+d4CooFu72UXWej/1PSJrPSIi0hyPEBEREZHiMRARERGR4jEQERERkeIxEBEREZHicVA1UQEwfYe8A7enf8eB20REn4NHiIiIiEjxGIiIiIhI8RiIiIiISPEYiIiIiEjxGIiIiIhI8RiIiIiISPEYiIiIiEjxGIiIiIhI8RiIiIiISPEYiIiIiEjxGIiIiIhI8fI1EJ08eRIdO3ZEmTJloFKpsG/fPrX7hRCYOnUqrK2tYWxsDGdnZ9y5c0dtn5cvX8LNzQ0WFhYoUqQIPDw8kJCQoLbPlStX8PXXX8PIyAg2NjaYP3++th8aERERFSL5GojevHmDOnXqYOXKlTneP3/+fCxbtgxr1qzBuXPnYGpqChcXFyQlJUn7uLm5ISIiAseOHcOBAwdw8uRJ/Pjjj9L98fHxaNu2LcqXL4/Q0FD89ttvmD59On7//XetPz4iIiIqHPJ1tfv27dujffv2Od4nhMCSJUswZcoUdO7cGQCwadMmWFlZYd++fejVqxdu3LiBw4cP48KFC2jYsCEAYPny5fj222+xYMEClClTBlu2bEFKSgo2bNgAAwMD1KxZE2FhYVi0aJFacCIiIiLlKrBjiCIjIxEVFQVnZ2dpm6WlJZo0aYKQkBAAQEhICIoUKSKFIQBwdnaGjo4Ozp07J+3TokULGBgYSPu4uLjg1q1bePXqVY5tJycnIz4+Xu1GREREX64CG4iioqIAAFZWVmrbrayspPuioqJQqlQptfv19PRQrFgxtX1yqpG1jfd5eXnB0tJSutnY2Gj+gIiIiKjAKrCBKD9NnjwZcXFx0u3x48f53SUiIiLSonwdQ/QxpUuXBgBER0fD2tpa2h4dHY26detK+8TExKj9XlpaGl6+fCn9funSpREdHa22T+bPmfu8z9DQEIaGhrI8DqKCoP3/usta71Dn3dm2fbt3tqxt/NV1iqz1iIg+psAeIapYsSJKly4Nf39/aVt8fDzOnTsHR0dHAICjoyNiY2MRGhoq7XPixAlkZGSgSZMm0j4nT55EamqqtM+xY8dQvXp1FC1aNI8eDRERERVk+RqIEhISEBYWhrCwMADvBlKHhYXh0aNHUKlUGD16NGbPno0///wTV69eRb9+/VCmTBl06dIFAGBnZ4d27dph8ODBOH/+PIKDgzFixAj06tULZcqUAQD07t0bBgYG8PDwQEREBLZv346lS5di7Nix+fSoiYiIqKDJ11NmFy9eROvWraWfM0NK//794evriwkTJuDNmzf48ccfERsbi6+++gqHDx+GkZGR9DtbtmzBiBEj0KZNG+jo6KB79+5YtmyZdL+lpSWOHj2K4cOHo0GDBihRogSmTp3KS+6JiIhIkq+BqFWrVhBCfPB+lUqFmTNnYubMmR/cp1ixYti6detH26lduzZOnTqV634SERHRl63AjiEiIiIiyisMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4+bqWGRHR53Dds1rWege7DZW1HhEVXjxCRERERIrHQERERESKx0BEREREisdARERERIrHQERERESKx0BEREREisdARERERIrHQERERESKx4kZiYiy6LBri6z1DvRwk7UeEWkHjxARERGR4jEQERERkeIxEBEREZHiMRARERGR4nFQNRFRHuu0a7+s9f7s0VHWekRKxCNEREREpHgMRERERKR4PGVGRPSF6br7tKz19nb/StZ6RAURjxARERGR4jEQERERkeIxEBEREZHiMRARERGR4jEQERERkeIxEBEREZHiMRARERGR4jEQERERkeIxEBEREZHi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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "genre_frequency_df = pd.DataFrame([genre_frequency]).T.reset_index()\n",
    "genre_frequency_df.columns = ['genre', 'count']\n",
    "\n",
    "sns.barplot(x='genre', y='count', data=genre_frequency_df.sort_values(by='count', ascending=False))\n",
    "plt.xticks(rotation=90)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f6b9b2cb",
   "metadata": {},
   "source": [
    "### Data Preprocessing\n",
    "We are going to use \"Colaborative Filtering\" for this step. Colaborative filtering is based on the ideat that similar people like similar movies.\n",
    "\n",
    "We are goin tho transform our data into \"user-item\" matrix. Since it does not require any information about user or items to generate recommendation, \n",
    "\n",
    "\n",
    "user_mapper: maps user id to user index,\n",
    "\n",
    "movie_mapper: maps movie id to movie index,\n",
    "\n",
    "user_inv_mapper: maps user index to user id,\n",
    "\n",
    "movie_inv_mapper: maps movie index to movie id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "3e17500f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.sparse import csr_matrix\n",
    "\n",
    "def create_X(df):\n",
    "    \"\"\"\n",
    "    Generates a sparse matrix from ratings dataframe.\n",
    "    \n",
    "    Args:\n",
    "        df: pandas dataframe containing 3 columns (userId, movieId, rating)\n",
    "    \n",
    "    Returns:\n",
    "        X: sparse matrix\n",
    "        user_mapper: dict that maps user id's to user indices\n",
    "        user_inv_mapper: dict that maps user indices to user id's\n",
    "        movie_mapper: dict that maps movie id's to movie indices\n",
    "        movie_inv_mapper: dict that maps movie indices to movie id's\n",
    "    \"\"\"\n",
    "    M = df['userId'].nunique()\n",
    "    N = df['movieId'].nunique()\n",
    "\n",
    "    user_mapper = dict(zip(np.unique(df[\"userId\"]), list(range(M))))\n",
    "    movie_mapper = dict(zip(np.unique(df[\"movieId\"]), list(range(N))))\n",
    "    \n",
    "    user_inv_mapper = dict(zip(list(range(M)), np.unique(df[\"userId\"])))\n",
    "    movie_inv_mapper = dict(zip(list(range(N)), np.unique(df[\"movieId\"])))\n",
    "    \n",
    "    user_index = [user_mapper[i] for i in df['userId']]\n",
    "    item_index = [movie_mapper[i] for i in df['movieId']]\n",
    "\n",
    "    X = csr_matrix((df[\"rating\"], (user_index,item_index)), shape=(M,N))\n",
    "    \n",
    "    return X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper\n",
    "\n",
    "X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_X(ratings)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "1cd08b74",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(610, 9724)"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99980b6c",
   "metadata": {},
   "source": [
    "Matrix contains 610 Users and 9724 movies"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de496211",
   "metadata": {},
   "source": [
    "### Data Sparsity\n",
    "    \n",
    "Now, we need to evaluate the sparsity of our utility matrix to understand if we can use Collaborative Filtering as a Recommender System\n",
    "\n",
    "sparsity = #zero values / total elements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "d7b1aec9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix sparsity: 1.7%\n"
     ]
    }
   ],
   "source": [
    "n_total = X.shape[0]*X.shape[1]\n",
    "n_ratings = X.nnz\n",
    "sparsity = n_ratings/n_total\n",
    "print(f\"Matrix sparsity: {round(sparsity*100,2)}%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6292b115",
   "metadata": {},
   "source": [
    "### Cold Start Problem\n",
    "\n",
    "The cold start problem in collaborative filtering refers to the challenge of making accurate recommendations for new users or new items when there is little or no historical interaction data. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "c6be02bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "610"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n_ratings_per_user = X.getnnz(axis=1)\n",
    "len(n_ratings_per_user)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "2c2a4015",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Most active user rated 2698 movies.\n",
      "Least active user rated 20 movies.\n"
     ]
    }
   ],
   "source": [
    "print(f\"Most active user rated {n_ratings_per_user.max()} movies.\")\n",
    "print(f\"Least active user rated {n_ratings_per_user.min()} movies.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "00fc23e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9724"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n_ratings_per_movie = X.getnnz(axis=0)\n",
    "len(n_ratings_per_movie)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "d2b3ac53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Most rated movie has 329 ratings.\n",
      "Least rated movie has 1 ratings.\n"
     ]
    }
   ],
   "source": [
    "print(f\"Most rated movie has {n_ratings_per_movie.max()} ratings.\")\n",
    "print(f\"Least rated movie has {n_ratings_per_movie.min()} ratings.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "73fdec75",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABO4AAAK+CAYAAAAVJlF+AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/NK7nSAAAACXBIWXMAAA9hAAAPYQGoP6dpAAC/NklEQVR4nOzde3jT5f3/8VfyybGlLYdKC8oAETkIgqDWIh7Xy7I5sZsi4ibI+OJ+KorrxAkiRdF1Q1FQmKgbik4UUcacOhQ72JwUGCdPEyYOrYItINDQ0jY9fH5/lARD09KmaZK2z8d15XJ8cueTOyl8f/fv1ff7vi2maZoCAAAAAAAAEFOs0Z4AAAAAAAAAgLoI7gAAAAAAAIAYRHAHAAAAAAAAxCCCOwAAAAAAACAGEdwBAAAAAAAAMYjgDgAAAAAAAIhBBHcAAAAAAABADCK4AwAAAAAAAGIQwR0AAAAAAAAQgwjuAAR10003yWKx6Isvvoj2VMLinXfe0YUXXqhOnTrJYrEoKysr2lM6qV69eqlXr17RngYAAGilWM9FH+u59oWfN1oCwR3Qwr744gtZLBZZLBZlZmYGHbNhwwZZLBbddNNNkZ1cO/HFF1/o6quv1v/+9z9NnDhROTk5uv766xt8zezZs/0/N98jLi5OgwYN0r333iuPx9PsebW1xbTPc889V+e7c7vd6t+/v7Kzs3XgwIGIz2ndunUn/TfWmDEAgPaJ9Vz0sZ6LrFhcz33332FqaqqqqqqCjvv000/94wjR0BbYoj0BoD1555139Pe//12XX355tKfSrrz77rsqLy/XvHnzdMMNNzTptddcc40GDRokSSoqKtJbb72l3/zmN3rjjTe0adMmOZ3OlpiyJCkvL6/F7h0J3//+9zVy5EhJ0v79+/X222/rscce08qVK7VlyxZ16dIlyjMEAKDpWM9FB+u56IjF9ZzNZvP/HEePHl3n+T/+8Y+yWqNTo9Taf96ITQR3QIT06tVLBQUF+vWvf61NmzbJYrFEe0rtxt69eyVJ3bt3b/Jrr7322oDf5paXl+uCCy7QBx98oGXLlmnixIlhm+eJ+vTp02L3joSMjAzdc889/j9XVlYqMzNTa9eu1RNPPKHZs2dHb3IAAISA9Vz0sJ6Ljlhcz40YMUIffPCBlixZUie4q6qq0p/+9CdlZGToH//4R8Tn1tp/3ohNtMoCEdKvXz/deOON2rx5s1555ZVGvaahPRIuvfTSOotFXzvAunXr9Oyzz2rw4MFyu93q3bu3Hn/8cUmSaZqaN2+e+vXrJ5fLpb59++r555+vdw41NTWaO3eu+vbtK5fLpd69e+uBBx5QZWVl0PH//Oc/ddVVVyk5OVlOp1N9+/bVzJkzdfTo0YBxvrbE2bNna/369briiivUsWPHRi+AP/74Y1133XXq2rWrnE6nevfurTvvvFPffvutf4yvnD4nJ0eSdNlll/nL5tetW9eo9zmRy+XST3/6U0nSli1bAp7bu3evcnJydMEFF/jn1atXL916663at29fwNhevXpp6dKlkqTevXv753XppZcGjDnx5//dn/GyZcs0dOhQud1udevWTVOnTlVZWVmdOVdVVSk3N1d9+vSRy+XSGWecodzcXP3vf/8L2tLz2WefaeLEierdu7ecTqc6d+6sIUOG6M4775RpmiF9b5Jkt9v1i1/8QpL073//23/d6/Xq0Ucf1bBhwxQfH6+EhARddNFFev311+vcw9eO8r///U/z5s3TwIED5XQ6W7QtqSnfx5EjR5STk6OzzjpLbrdbHTt2VGZmpv71r3/Vua/v33B5eblmzpypPn36yG63E2gCQAxjPcd67rtYz0VnPed2u3X99dfrzTffrPMzeeONN1RUVKSf//zn9b6+tLRUOTk56t+/v1wulzp37qwrr7xS77//fsC4OXPmyGKx1Ptva+XKlbJYLLr33nv91+r7926appYsWaILL7xQiYmJiouL07nnnqslS5Y06jOjfaPiDoigBx54QC+//LJmzpypn/zkJ7Lb7S3yPvPnz9e6det09dVX6/LLL9drr72mqVOnKi4uTtu2bdNrr72mH/3oR/r+97+vl19+WRMmTFCvXr108cUX17nXnXfeqffff1/XXXedOnTooL/+9a/KycnRhx9+qFdffTVg7JNPPqnbbrtNHTt21FVXXaWuXbtq8+bNeuihh7R27VqtXbtWDocj4DXr16/Xb37zG1122WW6+eabVVBQcNLP969//UuZmZnyer269tpr1atXL+Xn52vBggV64403tGHDBiUnJ6tjx47KycnRunXr9I9//MP/OSWFZb8Lmy3w/4T+85//1Lx58/T9739faWlpstvt2rZtm5588km9/fbb2rp1q5KSkiTVfq/PPfecPvjgA02dOlUdO3Zs0rwWLlyo1atX+3/Gq1ev1uOPP64DBw7oxRdfDBj785//XC+88IJOP/103XbbbaqoqNBjjz2m/Pz8Ovfdu3evzj//fJWWlurKK6/U2LFjVVpaqs8++0y///3v9cgjj9T53KHwLegrKio0atQorVu3TkOHDtWkSZNUWVmpN998U1dffbWeeOIJTZkypc7rb7/9dm3YsEFXXnml/+9aS2jK93Hw4EFdfPHF+uSTT3ThhRfq//2//yePx6O//OUvuuyyy7RixYqgm2hfc801+uCDDzRq1Ch17NhRvXv3bpHPAgAID9ZzrOdYz9WK5nru5z//uZ566im98MIL+tWvfuW/vmTJEnXu3Lneg0vKy8t1+eWXa9OmTRo2bJjuvPNOFRUVafny5Xr77bf10ksvacyYMZKkn/3sZ8rJydGf/vQnjR8/vs69XnjhBUnSjTfe2OBcTdPUT3/6U7300kvq27evbrjhBjkcDq1Zs0aTJk3Sf/7zHz3yyCON/uxoh0wALWr37t2mJDMzM9M0TdO86667TEnmE0884R+Tn59vSjInTJgQ8NqePXuaPXv2DHrfSy65xDzxn3BOTo4pyezcubP5+eef+68XFBSYDofDTEpKMs8880xz3759/uc2bNhgSjKvuuqqgHtNmDDBlGSecsop5ldffeW/XlFRYV588cWmJPPVV1/1X//kk09Mm81mDhkyxDxw4EDAvXJzc01J5iOPPOK/tnbtWlOSKclcsmRJ0M8YTHV1tdmnTx9Tkrl69eqA56ZNm2ZKMn/+858H/V7Wrl3b6Pfxveall14KuF5WVmYOGTLElGSuWLEi4LmioiLzyJEjde61dOlSU5L54IMPBlz3fce7d+8OOodgP3/fvJKSkswdO3b4rx89etQ888wzTavVau7Zs8d//d133zUlmUOHDjVLS0v91/fu3WumpKTU+Xv3+OOPm5LM+fPn15nPt99+G3SeJ3r22WdNSWZubm7A9crKSvPyyy83JZn333+/aZqmOWPGDFOSed9995k1NTX+sR6Pxzz33HNNh8MR8Hl839lpp51mfvnll42aj2ke//t24r+xk41pyvdxww03mJLMZ555JuB6UVGR2aNHD/OUU04xy8rK/Nd9/4aHDh3a6O8WABAdrOdYz7GeqxXN9dyJ/w4HDRpknnXWWf7nv/nmG9Nms5m33367aZqm6XQ663z3999/vynJ/OlPfxow161bt5oOh8Ps2LGj6fF4/NdHjhxpGoZh7t27N+A+3377relwOMxzzz034Hqwn/fTTz9tSjInTpxoer1e//WKigrzqquuMiWZmzdvbvT3gPaHVlkgwmbMmKGOHTtqzpw5KikpaZH3mDp1qk4//XT/n3v06KGRI0equLhY9957r0455RT/c2lpaTr99NP1wQcf1Huv0047zf9nh8Ohhx56SFLtaVM+Tz31lKqqqvTEE0/U2aT27rvv1imnnKKXXnqpzv2HDRvWpH1F3n//fX3++ef6wQ9+UOdUt1mzZqlz585atmyZvF5vo+/ZkFdffVWzZ8/W7Nmzdeutt6pfv3764IMP9OMf/1g/+clPAsZ27dpVHTp0qHOPG2+8UYmJiXr33XfDMiep9ufSr18//5/dbrfGjRunmpqagJaPP/3pT5Jqv5u4uDj/dV8rRn3cbneda507d27SHN99913/d3f77bdr4MCB+vvf/67evXtrypQpqqmp0ZNPPqk+ffro/vvvD2irSUhI0KxZs+T1erVy5co69542bZq+973vNWk+zXGy7+PAgQNavny5Lr/8cv3f//1fwLiuXbtq2rRp2r9/f9C/A/fff3+Tv1sAQHSxngvEei40rOeat577+c9/rk8++UQbN26UJC1dulRVVVUNtskuXbpUdrtdv/3tbwPmes4552jChAk6fPiwVq1a5b9+4403qrq6us7f++XLl8vr9epnP/vZSee5cOFCxcfHa9GiRQEVut/9dxjs3xXgQ6ssEGGdOnXSPffco3vuuUePPPJIi+xnNXTo0DrXunXr1uBzvv8H70QXXXRRnWvp6emy2Wzatm2b/9qGDRskSW+//XbQ05Tsdrt27NhR5/p5550X9H3r43vP7+4d4tOhQwede+65euedd7Rz504NHjy4SfcO5rXXXtNrr70WcG3MmDFavnx50P1bVq5cqaeeekpbt27VoUOHVF1d7X/Ot6lyOAwfPrzONd+C/PDhw/5rvgW87zSw77rwwgvrXLvqqqs0ffp03XbbbcrLy9OoUaN0ySWXBPx/HBorLy/P/3fBtz9Mdna2pk+frs6dO+vTTz/VoUOH1L17d91///11Xr9//35JCvr35vzzz2/yfELR2O/j3//+t6qrq1VRURH03/Rnn30mqfaz/OhHPwp4LlKf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lVeUlpamv/71rwF7ur3wwgt66qmndPHFF6tPnz5KTEzUf/7zH7311lvq3Llzk06Ma4z7779fW7du1eOPP64333xTF198sbp27ao9e/boo48+0gcffKD8/PyT7h/SGPPmzdPGjRt1//3364033tAll1wil8ul//73v3r99ddlmqZefPFFdezY0f+apnwfv//977Vz507dfffdeuGFF5Senq6OHTvqq6++0ubNm/XZZ5/pm2++CTgNDgDQ+rGeazrWc03Deq5h5557rs4999xGjb377rv15ptv6oUXXtCnn36q73//+9q3b5+WL1+uqqoqPfPMM0pISKjzuhtvvFG///3vNWvWLP+fG+sXv/iFNmzYoKVLl+r9999XRkaGunfvrqKiIu3YsUMbN27UsmXL1KtXr0bfE+2MCaBF7d6925RkZmZmBn3+/fffNyWZkswJEybUef7vf/+7mZaWZjqdTrNLly7mjTfeaBYVFZmXXHKJeeI/4ZycHFOSuXbt2jr3mTBhginJ3L17d53ngt3LN/7zzz83f/vb35pnnHGG6XA4zJ49e5qzZ882Kyoqgn6eTZs2mddff73ZvXt30263m8nJyeawYcPMe+65x/z000/949auXWtKMnNycoLe52Q+/PBD89prrzWTk5NNu91u9uzZ05w6daq5f//+OmMb+l7q43vNSy+9VO+Yc88915Rk5uXlmaZpml6v13zooYfMvn37mk6n0/ze975n/upXvzKPHDli9uzZ0+zZs2ede8ydO9fs27evabfbTUnmJZdc4n8u2Gsa+izPPvusKcl89tlnA65XVlaac+bMMXv37m06HA7z9NNPN3/zm9+YGzduNCWZU6dO9Y/dsGGD+Ytf/MIcNGiQ2bFjR9Ptdpt9+/Y1p0yZYn755Zcn+9oC5pGbm9uo8VVVVeZTTz1lXnjhhWZiYqL/uxs1apT55JNPmiUlJf6xDf09bozDhw+bOTk55pAhQ8z4+HjTbrebPXr0MG+44QZz69atdcY39fs4evSoOXfuXHP48OFmfHy86Xa7zd69e5tZWVnm888/b1ZWVvrHBvt3BwCITaznWM+xnmtYJNZzJ/t3eCKn0xn051VSUmLed9995plnnmk6HA6zY8eO5g9+8APzvffea/B+ffv2NSWZp512mlldXR10TH1/R0zTNJcvX25mZGSYnTp1Mu12u3nqqaeal156qTlv3rygf+cBH4tpBunnAQC0eX/4wx80efJk/2/WAQAA0LqwngPaPoI7AGjjCgsLlZKSEnBy1549e3ThhRfq66+/1u7du9WjR48ozhAAAAANYT0HtF/scQcAbdxvf/tbvfnmm7rooovUtWtXFRQU6I033tCRI0c0e/ZsFnkAAAAxjvUc0H4R3AFAGzdq1Cj95z//0ZtvvqlDhw7J5XLp7LPP1q233qobbrgh2tMDAADASbCeA9ovWmUBAAAAAACAGGQ9+RAAAAAAAAAAkUZwBwAAAAAAAMQg9rhrQTU1Ndq7d68SEhICTv8BAACoj2maOnLkiLp37y6rld+xxirWeQAAoKlCWecR3LWgvXv3croPAAAIyVdffaXTTjst2tNAPVjnAQCAUDVlnUdw14ISEhIk1f5AEhMTozwbAADQGng8HvXo0cO/jkBsYp0HAACaKpR1HsFdC/K1TSQmJrKgAwAATUL7ZWxjnQcAAELVlHUeG6cAAAAAAAAAMYjgDgAAAAAAAIhBBHcAAAAAAABADCK4AwAAAAAAAGIQwR0AAAAAAAAQgwjuAAAAAAAAgBhEcAcAAAAAAADEIII7AAAAAAAAIAYR3AEAAAAAAAAxiOAOAAAAAAAAiEEEdwAAAAAAAEAMIrgDAAAAAAAAYhDBHQAAAAAAABCDCO4AAAAAAACAGERwBwAAAAAAAMQggjsAAAAAAAAgBhHcAQAAAAAAADGI4A4AAAAAAACIQQR3AAAAAAAAQAwiuAMAAAAAAABiEMEdAAAAAAAAEIMI7gAAAAAAAIAYRHAHAAAAAAAAxCCCOwAAAAAAACAGEdwBAAAAAAAAMYjgLkaUeatVXWNGexoAAAAIgbeqRlXVNdGeBgAAaGMI7mJATY2pzPn/1KK1u6I9FQAAAITgtmVb9du/7Yj2NAAAQBtDcBcDNuz+VgUHjypvR1G0pwIAAIAQ7NpXom+Ky6M9DQAA0MYQ3MWAVdv2SJI++rpYnvLKKM8GAAAATXWw1Ksyb1W0pwEAANoYgrsoK6+s1lsfFerCM5JVY0r/3n0w2lMCAABAE1RV18hTVqmjlexxBwAAwovgLsr+vmOfSiqqdM05p+qUDk6t//zbaE8JAAAATXC4rFKmRMUdAAAIO4K7KPvztj0645R4devo1sDuifrXrgPRnhIAAACa4GCpV5JUVlkd5ZkAAIC2huAuig4f9Wrtjn0acUayJOms7onaWXhE35ZURHlmAAAAaKxvS2qDu3JaZQEAQJgR3EXRmx99oxrTVPrpXSRJA7slSpI2/I997gAAAFoLX8VdORV3AAAgzAjuomh7wWGdnhyvjnEOSVKXDk517+jS+s9plwUAAGgtDh6lVRYAALQMgrsoKvKUq3O8M+DawG6Jep997gAAAFqNgyVU3AEAgJZBcBdF3xSXq2OcPeDaWd2T9MW3R/VNcVmUZgUAAICmOFhauz9xZbWpqmr2uQMAAOFDcBdF+45UqHO8I+Ba7+R4SdLn+0qjMSUAAAA00bfH9riTpPIqgjsAABA+MRHcLVq0SL169ZLL5VJaWpo2bdrU4PgVK1aof//+crlcGjx4sN56662A503T1KxZs9StWze53W5lZGTos88+CxgzevRofe9735PL5VK3bt104403au/evf7nv/jiC1ksljqPDRs2hOUzl1dWq7isUp3iAoM7358LPeVheR8AAAC0rG9LvHIYtctq2mUBAEA4RT24W758ubKzs5WTk6OtW7dqyJAhyszM1L59+4KOX79+vcaNG6dJkyZp27ZtysrKUlZWlj7++GP/mLlz5+rxxx/X4sWLtXHjRsXHxyszM1Pl5cfDsMsuu0yvvPKKdu7cqddee02ff/65rr322jrv9+677+qbb77xP4YPHx6Wz110LJg7seLOYbMq0WXzPw8AAIDY9m1phZITatd0ZV6COwAAED5RD+4effRRTZ48WRMnTtTAgQO1ePFixcXFacmSJUHHL1iwQKNGjdK0adM0YMAAzZkzR8OGDdPChQsl1VbbzZ8/XzNnztTVV1+ts88+W88//7z27t2rVatW+e/zy1/+UhdccIF69uypESNG6J577tGGDRtUWVkZ8H5dunRRamqq/2G3B+5J910VFRXyeDwBj/oUeWr3Qjmx4s53bR/BHQAAQKtw6GilkjvUHjhGxR0AAAinqAZ3Xq9XW7ZsUUZGhv+a1WpVRkaG8vPzg74mPz8/YLwkZWZm+sfv3r1bhYWFAWOSkpKUlpZW7z0PHjyoF198USNGjKgTzI0ePVpdu3bVyJEj9frrrzf4eXJzc5WUlOR/9OjRo96xvlbYTvF1g8COcXZaZQEAAFoB0zR1qNTrD+7KCO4AAEAYRTW4O3DggKqrq5WSkhJwPSUlRYWFhUFfU1hY2OB4338bc89f//rXio+PV5cuXVRQUKC//OUv/uc6dOigefPmacWKFXrzzTc1cuRIZWVlNRjeTZ8+XcXFxf7HV199Ve/YfZ5yue2G4hy2Os91inMQ3AEAALQCnvIqVdWY6hJPqywAAAi/qLfKRtO0adO0bds2vfPOOzIMQ+PHj5dpmpKk5ORkZWdnKy0tTeedd55++9vf6mc/+5kefvjheu/ndDqVmJgY8KhPYXF50Go7SeoU7/C30gIAACB2HTpae6LsKQlU3AEAgPCrW+4VQcnJyTIMQ0VFRQHXi4qKlJqaGvQ1qampDY73/beoqEjdunULGDN06NA675+cnKwzzzxTAwYMUI8ePbRhwwalp6cHfe+0tDStWbOmSZ+xPoWe8qD720lSpzi7DhypUE2NKavVEpb3AwAAQPgdKq39ZSt73AEAgJYQ1Yo7h8Oh4cOHKy8vz3+tpqZGeXl59YZn6enpAeMlac2aNf7xvXv3VmpqasAYj8ejjRs31ntP3/tKtQdM1Gf79u0BYWBzFHnK1bG+4C7eoaoaU9+WesPyXgAAAGgZh45WSfpucFcTzekAAIA2JqoVd5KUnZ2tCRMm6Nxzz9X555+v+fPnq7S0VBMnTpQkjR8/Xqeeeqpyc3MlSVOnTtUll1yiefPm6corr9TLL7+szZs36+mnn5YkWSwW3XnnnXrwwQfVt29f9e7dW/fdd5+6d++urKwsSdLGjRv173//WyNHjlSnTp30+eef67777lOfPn384d7SpUvlcDh0zjnnSJJWrlypJUuW6A9/+ENYPndhcbmG9ugY9DlfJV6Rp9zfdgEAAIDY46u46xzvkEW0ygIAgPCKenA3duxY7d+/X7NmzVJhYaGGDh2q1atX+w+XKCgokNV6vDBwxIgRWrZsmWbOnKkZM2aob9++WrVqlQYNGuQfc/fdd6u0tFQ333yzDh8+rJEjR2r16tVyuVySpLi4OK1cuVI5OTkqLS1Vt27dNGrUKM2cOVNO5/GgbM6cOfryyy9ls9nUv39/LV++XNdee22zP7NpmiryVKhTfH2tsseDu0GnJjX7/QAAANAyDh71KsFlk2G1yGGzcjgFAAAIK4vpO40BYefxeJSUlKTi4uKAgyoOH/Vq6ANrdOf3+yrt9C51XldTY+rGJRv1YNZg3ZD2vUhOGQAARFl96wfEFt/P6d7lG/X3/x3RvDFD9YsXNusXl/TRbZedEe3pAQCAGBTKOq9dnyobLYWeckmqt+LOarWoY5zDPw4AAACx6VCpVwkuuyTJaTc4nAIAAIQVwV0UFHlq90Kp71TZ2ufs2kdwBwAAENMOHvUqwVm7+4zDoFUWAACEF8FdFBQVH6u4i7PXO6ZTnENFBHcAAAAx7WBppRLdxyrubFYOpwAAAGFFcBcFhZ5yJbntshn1f/0d4xz6ppjgDgAAIJYdOlqhRNexijubVeWVNVGeEQAAaEsI7qKgyFOuzvXsb+fTOd5BqywAAECMO3S00r/HncOwsscdAAAIK4K7KCj0lKuju/42Wam2jfbg0Up5q/itLQAAQKyqqKxRwncq7sq8VVGeEQAAaEsI7qKgqLi83hNlfXwHV+w7QtUdAABALEv0VdzZrDpKqywAAAgjgrsoKPSUN3iirCR/K63vBFoAAID2atGiRerVq5dcLpfS0tK0adOmBsevWLFC/fv3l8vl0uDBg/XWW28FPG+xWII+Hn744ZDmF3A4BRV3AAAgjAjuIqyyukbflnjVKf5krbLHKu7Y5w4AALRjy5cvV3Z2tnJycrR161YNGTJEmZmZ2rdvX9Dx69ev17hx4zRp0iRt27ZNWVlZysrK0scff+wf88033wQ8lixZIovFomuuuSakOR4/nMLgVFkAABBWBHcRdqCkQqakziepuIt3GrIbFhUS3AEAgHbs0Ucf1eTJkzVx4kQNHDhQixcvVlxcnJYsWRJ0/IIFCzRq1ChNmzZNAwYM0Jw5czRs2DAtXLjQPyY1NTXg8Ze//EWXXXaZTj/99JDm2OFYcOfkVFkAABBmBHcRVlhcG8SdbI87i8WiLvFOWmUBAEC75fV6tWXLFmVkZPivWa1WZWRkKD8/P+hr8vPzA8ZLUmZmZr3ji4qK9Oabb2rSpEkNzqWiokIejyfg4WO31i6pHTZOlQUAAOFFcBdhB0u9ko5vYtyQjnF2FVFxBwAA2qkDBw6ourpaKSkpAddTUlJUWFgY9DWFhYVNGr906VIlJCToJz/5SYNzyc3NVVJSkv/Ro0cPSZLVIlmtFkmSw7DSKgsAAMKK4C7CPOWVkqQOTttJx3aMs/sr9AAAABB+S5Ys0U9/+lO5XK4Gx02fPl3FxcX+x1dffSVJMo6FdpKvVZbgDgAAhM/J0yOElaesSjarRXbDctKxneMc2lF4JAKzAgAAiD3JyckyDENFRUUB14uKipSamhr0NampqY0e/95772nnzp1avnz5SefidDrldDrrXP9ucOewWVVZbaqqukY2g9+PAwCA5mNFEWGeskp1cNpksZw8uEuKc2h/CXvcAQCA9snhcGj48OHKy8vzX6upqVFeXp7S09ODviY9PT1gvCStWbMm6Pg//vGPGj58uIYMGRLyHG1GYMWdJJVXcUAFAAAID4K7CPOUVyrOaTRqbAenTUfKq1RdY7bwrAAAAGJTdna2nnnmGS1dulSffvqpbrnlFpWWlmrixImSpPHjx2v69On+8VOnTtXq1as1b9487dixQ7Nnz9bmzZs1ZcqUgPt6PB6tWLFC//d//9es+RmW71bc1a7xyry0ywIAgPCgVTbCissqFe9o3Nfu2wfPU1Z50lNoAQAA2qKxY8dq//79mjVrlgoLCzV06FCtXr3afwBFQUGBrNbjv4seMWKEli1bppkzZ2rGjBnq27evVq1apUGDBgXc9+WXX5Zpmho3blyz5mezBqm4Y587AAAQJgR3EeYpq1Kco7EVd7XjDhPcAQCAdmzKlCl1KuZ81q1bV+famDFjNGbMmAbvefPNN+vmm29u9txO3ONOIrgDAADhQ6tshBWXVSqukRV38ccq7g4f9bbklAAAABAi4zvVfr7grozgDgAAhAnBXYR5yiubUHF3LLgrq2zJKQEAACBE3624cx47SZY97gAAQLgQ3EWYp6zSX0l3Mh1cteOKjxLcAQAAxKJgrbJU3AEAgHAhuIswT3nj97hzGFbZDQutsgAAADEq8HCK2jUee9wBAIBwIbiLINM0daS88XvcWSwWJTjttMoCAADEKCruAABASyK4i6BSb7VqzOOnxTZGvMvQYVplAQAAYpL1O8Gd3bDIIqm8siZ6EwIAAG0KwV0EFR+rnGtsxZ1Ue0BFMRV3AAAAMclmOR7cWSwWOe1WDqcAAABhQ3AXQZ5jAVx8UyruHDb2uAMAAIhR322VlWr3KKZVFgAAhAvBXQR5Qqi4i3fadIhWWQAAgJh0YnDntBkcTgEAAMKG4C6CPOVVktToU2Wl2lZZKu4AAABiU52KOxutsgAAIHwI7iIolIo79rgDAACIXTZr4HLaaaNVFgAAhA/BXQR5yivlMKxy2Br/tccfC+5qaswWnBkAAABCcUJuJ4fNyqmyAAAgbAjuIshTVqUOzsZX20m1FXc1plTirWqhWQEAACBUtiCtsuxxBwAAwoXgLoI85ZWKa8KJspLUwVUb9BVzQAUAAEDMCXqqLL9wBQAAYUJwF0HFZZVNOphCkr9C7zDBHQAAQMwJVnF3lFZZAAAQJgR3EeQpq2zSwRSS1OFYhd7hMk6WBQAAiDWGJTC4c9qouAMAAOFDcBdBoVTcxVNxBwAAELOsJ5xO4bAZnCoLAADChuAugjzlTa+4c9sNWS3S4TKCOwAAgFhjM4JU3BHcAQCAMCG4iyBPWZXim3g4hcViUYLLruKjtMoCAADEmjqHU9isqmCPOwAAECYEdxHkKa9UfBMr7qTaAypolQUAAIg9Jx5OQcUdAAAIJ4K7CKmpMVVSXqW4JlbcSVK806BVFgAAIAbVOVXWsKqc4A4AAIQJwV2ElHirZEohVdzFU3EHAAAQk6xBWmUrq01VVdMuCwAAmo/gLkKKjwVvTT1VVpI6OGw6zB53AAAAMcc44VRZp632z+VVBHcAAKD5CO4ixFNeG9zFO0OouHNRcQcAABCL6rTK2mp/SVvmpV0WAAA0H8FdhHjKqiSFWHHntOlwGRV3AAAAscaw1D2cQhL73AEAgLAguIsQf8VdiKfKFpdVyjTNcE8LAAAAzVC34o7gDgAAhA/BXYR4jp0KG8qpsh2cNlVWmypjAQgAABBTTjycwldxx7oNAACEA8FdhHjKq+SyW2WzNv0r9+2Lxz53AAAAscV2wu9k7Yav4o7DKQAAQPMR3EWIp6wypDZZqbbiTiK4AwAAiDUnniprHKvAq6omuAMAAM1HcBchnvLKkNpkpe8EdxxQAQAAEFOME1plfXveVdawNzEAAGg+grsIKS6rVFwzK+6KqbgDAACIKSceTuEL8iqrqLgDAADNR3AXIZ6yKsU5Qqu4i3MYskg6XEZwBwAAEEvqVNwd2+OuqobgDgAANB/BXYQUl3lDrrizWi2Kd9rY4w4AACDGGJbgrbLealplAQBA8xHcRYinrErxIVbcSbXtsuxxBwAAEFtsJxxOYeNwCgAAEEYEdxHiKa9UvDO0ijtJ6uAy2OMOAAAgxpzYKuvf447gDgAAhAHBXYQcKQ99jztJctttOlJeFcYZAQAAoLlODO4sFosMq0WVtMoCAIAwILiLANM0VVpRJbe9GcGdw5CnnIo7AACAWHJicCfVtstScQcAAMKB4C4CyiqrZUpyNSO4i7MT3AEAAMQawwge3FVRcQcAAMKA4C4CjlZUS2pmcOcwdKSMVlkAAIBYYgtScWdYLfJScQcAAMKA4C4CSr21gZvLHvrX7XYYOlJBcAcAABBLgrbKGlYq7gAAQFgQ3EXAUX9w15yKO5uO0CoLAAAQU2zWustp9rgDAADhQnAXAUe9zW+VdTsMlVfWqIpFIAAAQMwItpgmuAMAAOFCcBcBpb7gzhb61x3nqA39SmiXBQAAiBkWS/A97ipplQUAAGFAcBcBZccOp3A7mtcqK0lHygnuAAAAYpnNsFJxBwAAwoLgLgJ8h1M4bc07VVaSPOxzBwAAENMMq1RVQ3AHAACaj+AuAsq8VXIY1qCnjjVW3LH98ai4AwAAiG2G1SpvFa2yAACg+QjuIqDUW92sNlnpeJstwR0AAEBss1ktVNwBAICwILiLgKMV1XLZm/dVH9/jjlZZAACAWGZwqiwAAAgTgrsIKKuslqsZ+9tJksNmlc2wUHEHAAAQ4wwLp8oCAIDwILiLgJKKKjmbWXEn1e5zR8UdAABAbLMZFlVWUXEHAACaj+AuAsq8VXLZm1dxJ9W2y1JxBwAAENsMq0WV7HEHAADCgOAuAkq9zW+VlaQ4h6EjFQR3AAAAscxmtcpLxR0AAAiDmAjuFi1apF69esnlciktLU2bNm1qcPyKFSvUv39/uVwuDR48WG+99VbA86ZpatasWerWrZvcbrcyMjL02WefBYwZPXq0vve978nlcqlbt2668cYbtXfv3oAxH374oS666CK5XC716NFDc+fODenzlVZUh6VV1u0wqLgDAACIcbWnyrLHHQAAaL6oB3fLly9Xdna2cnJytHXrVg0ZMkSZmZnat29f0PHr16/XuHHjNGnSJG3btk1ZWVnKysrSxx9/7B8zd+5cPf7441q8eLE2btyo+Ph4ZWZmqry83D/msssu0yuvvKKdO3fqtdde0+eff65rr73W/7zH49EVV1yhnj17asuWLXr44Yc1e/ZsPf30003+jEe9VXKHoVXWbTd0pIw97gAAAGKZYbVQcQcAAMLCYppmVH8dmJaWpvPOO08LFy6UJNXU1KhHjx66/fbbdc8999QZP3bsWJWWluqNN97wX7vgggs0dOhQLV68WKZpqnv37vrVr36lu+66S5JUXFyslJQUPffcc7r++uuDzuP1119XVlaWKioqZLfb9eSTT+ree+9VYWGhHA6HJOmee+7RqlWrtGPHjkZ9No/Ho6SkJF1w/+s6r+9pGnf+95r03ZzoyXW7VFJRpZW3Xtis+wAAgNjlWz8UFxcrMTEx2tNBPXw/pzXbdis+ISHguefWf6EvDpTq7V9eHKXZAQCAWBTKOi+qFXder1dbtmxRRkaG/5rValVGRoby8/ODviY/Pz9gvCRlZmb6x+/evVuFhYUBY5KSkpSWllbvPQ8ePKgXX3xRI0aMkN1u97/PxRdf7A/tfO+zc+dOHTp0KOh9Kioq5PF4Ah6SdLSiWk5bGE6V5XAKAACAmGdYLaqspuIOAAA0X1SDuwMHDqi6ulopKSkB11NSUlRYWBj0NYWFhQ2O9/23Mff89a9/rfj4eHXp0kUFBQX6y1/+ctL3+e57nCg3N1dJSUn+R48ePSRJRyur5XaE6XAKgjsAAICYZuNUWQAAECZR3+MumqZNm6Zt27bpnXfekWEYGj9+vJrTOTx9+nQVFxf7H1999ZUkqaKyJiynytYeTsEedwAAALHMZrWosprDKQAAQPPZovnmycnJMgxDRUVFAdeLioqUmpoa9DWpqakNjvf9t6ioSN26dQsYM3To0Drvn5ycrDPPPFMDBgxQjx49tGHDBqWnp9f7Pt99jxM5nU45nc6gz7nCdKpsqbda1TWmDKul2fcDAABA+BlWi6polQUAAGEQ1Yo7h8Oh4cOHKy8vz3+tpqZGeXl5Sk9PD/qa9PT0gPGStGbNGv/43r17KzU1NWCMx+PRxo0b672n732l2n3qfO/zz3/+U5WVxyvc1qxZo379+qlTp05N/KSSKwynysbZa3PWkgraZQEAAGIVFXcAACBcot4qm52drWeeeUZLly7Vp59+qltuuUWlpaWaOHGiJGn8+PGaPn26f/zUqVO1evVqzZs3Tzt27NDs2bO1efNmTZkyRZJksVh055136sEHH9Trr7+ujz76SOPHj1f37t2VlZUlSdq4caMWLlyo7du368svv9Tf//53jRs3Tn369PGHezfccIMcDocmTZqkTz75RMuXL9eCBQuUnZ0d0ucMS3B3bJ88gjsAAIDYZTOsVNwBAICwiGqrrCSNHTtW+/fv16xZs1RYWKihQ4dq9erV/oMgCgoKZLUezxdHjBihZcuWaebMmZoxY4b69u2rVatWadCgQf4xd999t0pLS3XzzTfr8OHDGjlypFavXi2XyyVJiouL08qVK5WTk6PS0lJ169ZNo0aN0syZM/2trklJSXrnnXd02223afjw4UpOTtasWbN08803h/Q5wxnc1e5z5272/QAAABB+BhV3AAAgTCxmc05jQIM8Hk/t6bJ3vqL5N6arW1LzwrY9h8p016sfaMX/S9d5vTqHaZYAACCW+NYPxcXFSkxMjPZ0UA/fz2nNtt2KT0gIeC7v0yIteX+3/pd7ZZRmBwAAYlEo67yot8q2F+GouHMHVNwBAAAgFhlWi2pMqbqG348DAIDmIbiLEJctnK2y7HEHAAAQq2xG7RK7kn3uAABAMxHcRYjT3vyv2mmzymqRPAR3AAAAMcuwWCQR3AEAgOYjuIsAp90q67EFXHNYLBbFO220ygIAAMQwm1G77qvigAoAANBMBHcR4LKF72uOcxi0ygIAAMQww0rFHQAACA+CuwhwhmF/Ox+33aDiDgAAtCuLFi1Sr1695HK5lJaWpk2bNjU4fsWKFerfv79cLpcGDx6st956q86YTz/9VKNHj1ZSUpLi4+N13nnnqaCgICzztR0L7rwEdwAAoJkI7iLAdxpsuO5VQsUdAABoJ5YvX67s7Gzl5ORo69atGjJkiDIzM7Vv376g49evX69x48Zp0qRJ2rZtm7KyspSVlaWPP/7YP+bzzz/XyJEj1b9/f61bt04ffvih7rvvPrlcrrDM2Rfc0SoLAACai+AuApxhbJV1220cTgEAANqNRx99VJMnT9bEiRM1cOBALV68WHFxcVqyZEnQ8QsWLNCoUaM0bdo0DRgwQHPmzNGwYcO0cOFC/5h7771XP/zhDzV37lydc8456tOnj0aPHq2uXbuGZc6cKgsAAMKF4C4CHGHf445WWQAA0PZ5vV5t2bJFGRkZ/mtWq1UZGRnKz88P+pr8/PyA8ZKUmZnpH19TU6M333xTZ555pjIzM9W1a1elpaVp1apVDc6loqJCHo8n4FGf43vcUXEHAACah+AuAlxh3OMuzmHIU0bFHQAAaPsOHDig6upqpaSkBFxPSUlRYWFh0NcUFhY2OH7fvn0qKSnRb3/7W40aNUrvvPOOfvzjH+snP/mJ/vGPf9Q7l9zcXCUlJfkfPXr0qHesjcMpAABAmBDcRYDTHuaKuwoq7gAAAEJRU1Mbpl199dX65S9/qaFDh+qee+7Rj370Iy1evLje102fPl3FxcX+x1dffVXvWF/FXVUNwR0AAGgeW7Qn0B647OE8nMKmI+xxBwAA2oHk5GQZhqGioqKA60VFRUpNTQ36mtTU1AbHJycny2azaeDAgQFjBgwYoH/961/1zsXpdMrpdDZq3jZr7S9tvVW0ygIAgOah4i4CXGHe4660okqmyUIQAAC0bQ6HQ8OHD1deXp7/Wk1NjfLy8pSenh70Nenp6QHjJWnNmjX+8Q6HQ+edd5527twZMOa///2vevbsGZZ5U3EHAADChYq7CHCGseIuzmGoxpRKvdXq4OTHBwAA2rbs7GxNmDBB5557rs4//3zNnz9fpaWlmjhxoiRp/PjxOvXUU5WbmytJmjp1qi655BLNmzdPV155pV5++WVt3rxZTz/9tP+e06ZN09ixY3XxxRfrsssu0+rVq/XXv/5V69atC8ucbQZ73AEAgPAg+YmAcB9OIUlHyisJ7gAAQJs3duxY7d+/X7NmzVJhYaGGDh2q1atX+w+gKCgokNV6vLthxIgRWrZsmWbOnKkZM2aob9++WrVqlQYNGuQf8+Mf/1iLFy9Wbm6u7rjjDvXr10+vvfaaRo4cGZY52zhVFgAAhAnJTwS4HOFrlXXba39kJeVVUlLYbgsAABCzpkyZoilTpgR9LliV3JgxYzRmzJgG7/nzn/9cP//5z8MxvToMTpUFAABhwh53EeAywl9x5+GACgAAgJjkO5yiioo7AADQTAR3EeCwh/dwCqm2VRYAAACxx9cq66XiDgAANBPBXQS4w3g4hftYcFdSQcUdAABALLJaLbJaqLgDAADNR3AXAU5b+L5m17EQsIRWWQAAgJhlWC3scQcAAJqN4C4CXGGsuLNaLHLbDSruAAAAYpjNaiW4AwAAzUZwFwHOMAZ3Um27LMEdAABA7LIZFlXSKgsAAJqJ4C4CXGE8nEKq3TOPVlkAAIDYZbNaVEXFHQAAaCaCuwhwWMP7NcdRcQcAABDT2OMOAACEA8FdBFgslrDez2m36gjBHQAAQMyyWa2qrKFVFgAANA/BXStEqywAAEBsM6wWVVZRcQcAAJqH4K4V4lRZAACA2GYzLKqi4g4AADQTwV0r5HbYdKS8MtrTAAAAQD1sVou87HEHAACaieCuFaLiDgAAILYZnCoLAADCgOCuFXLbrexxBwAAEMNqT5WlVRYAADQPwV0r5HYYOuqtlmmyGAQAAIhFNquVVlkAANBsBHetkNthU1WNqQpOKgMAAIhJtMoCAIBwILhrhdx2Q5J0hHZZAACAmGSzWlTJL1kBAEAzEdy1Qm577Y+NAyoAAABik2G1qLKGbU0AAEDzENy1Qm6HTZJUSnAHAAAQk2xWi7xU3AEAgGYiuGuFaJUFAACIbYbVoioq7gAAQDMR3LVCbkdtcEerLAAAQGyyGVYq7gAAQLMR3LVCvoq7korKKM8EAAAAwXCqLAAACAeCu1bIblhkWC0qoVUWAAAgJtmsFlVW0yoLAACah+CuFbJYLIpzGCqpqI72VAAAABCEzWpRZQ0VdwAAoHkI7lopt92gVRYAACBGGVarKmmVBQAAzURw10q5HQatsgAAADHKZlhURassAABoJoK7VsplN3SEU2UBAABikmG1UHEHAACajeCulXLbDZUS3AEAAMQkm5WKOwAA0HwEd62U227oCK2yAAAAMclGxR0AAAgDgrtWyu0guAMAAIhVhtWqqhoq7gAAQPMQ3LVSLruhElplAQAAYpLNalFVjSnTJLwDAAChI7hrpdjjDgAAIHbZDIskqZJ97gAAQDMQ3LVScQ4q7gAAAGKVYfUFd+xzBwAAQkdw10q57YaOeqtVzd4pAAAAMcdmrV1mc7IsAABoDoK7VsplNyRJpV6q7gAAAGKNr+LOS8UdAABoBoK7VsrtqA3uSjhZFgAAIObYjgV3VTUEdwAAIHQEd61U3LHgjgMqAAAAYo9/j7sqWmUBAEDoCO5aKfexVtkjBHcAAAAxx3+qLBV3AACgGQjuWilaZQEAAGKXjVNlAQBAGBDctVK+wylKqLgDAACIOcaxU2VplQUAAM1BcNdKuQnuAAAAYpa/4o5WWQAA0AwEd62UYbXIabPSKgsAABCD/MFdFcEdAAAIHcFdKxbnMKi4AwAAiEG+U2WramiVBQAAoSO4a8XcdoI7AACAWGQzapfZXg6nAAAAzUBw14q5qbgDAACISf6Ku2oq7gAAQOgI7loxl91gjzsAAIAY5N/jjoo7AADQDAR3rZjbbqikvDLa0wAAAMAJDII7AAAQBgR3rZjbbugIrbIAAAAxx2b4gjtaZQEAQOgI7loxl8PQEVplAQAAYo5h8e1xR8UdAAAIHcFdK+a2Gyql4g4AACDmWCwW2awWWmUBAECzENy1YpwqCwAAELtshoVWWQAA0CwEd61YnJ1WWQAAgFhlUHEHAACaieCuFXPZDVXVmKqoqo72VAAAAHACu9Wqqhoq7gAAQOgI7loxt8OQJJVWENwBAADEGsNqkbeKijsAABA6grtWzG2vDe5KaJcFAACIOTbDoqoagjsAABC6mAjuFi1apF69esnlciktLU2bNm1qcPyKFSvUv39/uVwuDR48WG+99VbA86ZpatasWerWrZvcbrcyMjL02Wef+Z//4osvNGnSJPXu3Vtut1t9+vRRTk6OvF5vwBiLxVLnsWHDhvB++GbwVdwdqaiM8kwAAABwoto97miVBQAAoYt6cLd8+XJlZ2crJydHW7du1ZAhQ5SZmal9+/YFHb9+/XqNGzdOkyZN0rZt25SVlaWsrCx9/PHH/jFz587V448/rsWLF2vjxo2Kj49XZmamysvLJUk7duxQTU2NnnrqKX3yySd67LHHtHjxYs2YMaPO+7377rv65ptv/I/hw4e3zBcRAiruAAAAYpfNauVwCgAA0CxRD+4effRRTZ48WRMnTtTAgQO1ePFixcXFacmSJUHHL1iwQKNGjdK0adM0YMAAzZkzR8OGDdPChQsl1VbbzZ8/XzNnztTVV1+ts88+W88//7z27t2rVatWSZJGjRqlZ599VldccYVOP/10jR49WnfddZdWrlxZ5/26dOmi1NRU/8Nut7fYd9FU/j3uvAR3AAAAsYZTZQEAQHNFNbjzer3asmWLMjIy/NesVqsyMjKUn58f9DX5+fkB4yUpMzPTP3737t0qLCwMGJOUlKS0tLR67ylJxcXF6ty5c53ro0ePVteuXTVy5Ei9/vrrDX6eiooKeTyegEdL8lXcHaHiDgAAIObYrBZV0SoLAACaIarB3YEDB1RdXa2UlJSA6ykpKSosLAz6msLCwgbH+/7blHvu2rVLTzzxhH7xi1/4r3Xo0EHz5s3TihUr9Oabb2rkyJHKyspqMLzLzc1VUlKS/9GjR496x4aD02aV1SKVVBDcAQAAxBrDapGXijsAANAMtmhPINr27NmjUaNGacyYMZo8ebL/enJysrKzs/1/Pu+887R37149/PDDGj16dNB7TZ8+PeA1Ho+nRcM7i8Uit91gjzsAAIAYRMUdAABorqhW3CUnJ8swDBUVFQVcLyoqUmpqatDXpKamNjje99/G3HPv3r267LLLNGLECD399NMnnW9aWpp27dpV7/NOp1OJiYkBj5bmdhgqpeIOAAAg5rDHHQAAaK6oBncOh0PDhw9XXl6e/1pNTY3y8vKUnp4e9DXp6ekB4yVpzZo1/vG9e/dWampqwBiPx6ONGzcG3HPPnj269NJLNXz4cD377LOyWk/+VWzfvl3dunVr0mdsaW6HoSMEdwAAADHHsFpVScUdAABohqi3ymZnZ2vChAk699xzdf7552v+/PkqLS3VxIkTJUnjx4/XqaeeqtzcXEnS1KlTdckll2jevHm68sor9fLLL2vz5s3+ijmLxaI777xTDz74oPr27avevXvrvvvuU/fu3ZWVlSXpeGjXs2dPPfLII9q/f79/Pr6qvKVLl8rhcOicc86RJK1cuVJLlizRH/7wh0h9NY1CqywAAEBsslFxBwAAminqwd3YsWO1f/9+zZo1S4WFhRo6dKhWr17tP1yioKAgoBpuxIgRWrZsmWbOnKkZM2aob9++WrVqlQYNGuQfc/fdd6u0tFQ333yzDh8+rJEjR2r16tVyuVySaiv0du3apV27dum0004LmI9pHv+t6Jw5c/Tll1/KZrOpf//+Wr58ua699tqW/DqazGU3OJwCAAAgBhkGwR0AAGgei/ndpAph5fF4lJSUpDXbdis+IaFF3mP+u/+Vw2bVC5PSWuT+AAAgsnzrh+Li4ojsl4vQNGad9/u1u1ReVa0V/29EhGcHAABiUSjrvKjucYfmc9sNHaFVFgAAIObYDIu8VVTcAQCA0BHctXIuB3vcAQAAxCLDalFVDc0tAAAgdAR3rVwce9wBAIA2btGiRerVq5dcLpfS0tK0adOmBsevWLFC/fv3l8vl0uDBg/XWW28FPH/TTTfJYrEEPEaNGhX2edusViruAABAsxDctXJuh6FSgjsAANBGLV++XNnZ2crJydHWrVs1ZMgQZWZmat++fUHHr1+/XuPGjdOkSZO0bds2ZWVlKSsrSx9//HHAuFGjRumbb77xP1566aWwz91mUHEHAACah+CulXMfq7jjjBEAANAWPfroo5o8ebImTpyogQMHavHixYqLi9OSJUuCjl+wYIFGjRqladOmacCAAZozZ46GDRumhQsXBoxzOp1KTU31Pzp16hT2uRtWTpUFAADNQ3DXyrnshkxJR73V0Z4KAABAWHm9Xm3ZskUZGRn+a1arVRkZGcrPzw/6mvz8/IDxkpSZmVln/Lp169S1a1f169dPt9xyi7799tsG51JRUSGPxxPwOBmb1aLKan65CgAAQkdw18q5HYYk0S4LAADanAMHDqi6ulopKSkB11NSUlRYWBj0NYWFhScdP2rUKD3//PPKy8vT7373O/3jH//QD37wA1VX1/+L0NzcXCUlJfkfPXr0OOn8DauVijsAANAstmhPAM0TZ68N7o5UVKlrlOcCAADQGlx//fX+/z148GCdffbZ6tOnj9atW6fvf//7QV8zffp0ZWdn+//s8XhOGt7ZaJUFAADNRMVdK+eruCspp+IOAAC0LcnJyTIMQ0VFRQHXi4qKlJqaGvQ1qampTRovSaeffrqSk5O1a9euesc4nU4lJiYGPE7GZlhURassAABoBoK7Vs51rOKuhFZZAADQxjgcDg0fPlx5eXn+azU1NcrLy1N6enrQ16SnpweMl6Q1a9bUO16Svv76a3377bfq1q1beCZ+DIdTAACA5iK4a+X8FXcEdwAAoA3Kzs7WM888o6VLl+rTTz/VLbfcotLSUk2cOFGSNH78eE2fPt0/furUqVq9erXmzZunHTt2aPbs2dq8ebOmTJkiSSopKdG0adO0YcMGffHFF8rLy9PVV1+tM844Q5mZmWGdu81qVVWNKdOk6g4AAISGPe5aObedVlkAANB2jR07Vvv379esWbNUWFiooUOHavXq1f4DKAoKCmS1Hv9d9IgRI7Rs2TLNnDlTM2bMUN++fbVq1SoNGjRIkmQYhj788EMtXbpUhw8fVvfu3XXFFVdozpw5cjqdYZ27zWqRJFXVmLIblrDeGwAAtA8Ed62c3bDKbliouAMAAG3WlClT/BVzJ1q3bl2da2PGjNGYMWOCjne73Xr77bfDOb16GceCu8rqGtkNGl0AAEDTsYJoA9x2g+AOAAAgxtgMX3BHqywAAAgNwV0bEOewEdwBAADEmO9W3AEAAISC4K4NcDsM9rgDAACIMbZje+8R3AEAgFAR3LUBLruVijsAAIAY4z+cglZZAAAQIoK7NsBlN3SEijsAAICY4gvuvFTcAQCAEBHctQEcTgEAABB7fIdTUHEHAABCRXDXBrjtho6UV0Z7GgAAAPgOgz3uAABAMxHctQFuBxV3AAAAsYZWWQAA0FwEd20ArbIAAACxh8MpAABAcxHctQFuh6FSgjsAAICYYhwL7miVBQAAoSK4awPcdkPllTWqYlEIAAAQM2xG7VKbVlkAABAqgrs2wO0wJEmlFdVRngkAAAB8aJUFAADNRXDXBrjttcHdkQpOlgUAAIgVtMoCAIDmIrhrA3zBHRV3AAAAscNmENwBAIDmIbhrA3ytsiVU3AEAAMSM4xV3tMoCAIDQENy1Af5W2XJOlgUAAIgVhoWKOwAA0DwEd23A8Yo7gjsAAIBYYbFYZDMsqiK4AwAAISK4awNcNt8edwR3AAAAscRmtchLqywAAAgRwV0bYLVa5LYbtMoCAADEGJvVSsUdAAAIGcFdG+F2GLTKAgAAxBibYWGPOwAAEDKCuzbCbTdUQsUdAABATKFVFgAANAfBXRvhdlhV6iW4AwAAiCW0ygIAgOYguGsj3HYbe9wBAADEGMNKqywAAAgdwV0b4bJbCe4AAABijM1qUSWtsgAAIEQEd21E7amyldGeBgAAAL6DwykAAEBzENy1EW4HrbIAAACxhlZZAADQHAR3bUScw1BJBcEdAABALDGsFlXRKgsAAEJEcNdGuO2GSqi4AwAAiCk2q1VeKu4AAECICO7aCF/FnWnyG10AAIBYQassAABoDoK7NsLtMGRKKvVWR3sqAAAAOIZTZQEAQHMQ3LURcQ5DkmiXBQAAiCFU3AEAgOYguGsj3HabJOlIeWWUZwIAAAAfm9UibxXBHQAACA3BXRvhq7g7wsmyAAAAMcNmWFVVQ6ssAAAIDcFdG+H2BXe0ygIAAMQMg4o7AADQDAR3bQR73AEAAMQem9WiKva4AwAAISK4ayNcNl/FHXvcAQAAxAqDU2UBAEAzENy1EVarRW67oRL2uAMAAIgZNqtFXiruAABAiAju2pA4hyEPrbIAAAAxo/ZwCoI7AAAQGoK7NsTtMNjjDgAAIIbQKgsAAJqD4K4NiXMYKqlgjzsAAIBYYbNaVMmpsgAAIEQEd22Iy27oCBV3AAAAMcNmtaqqhoo7AAAQGoK7NsRNcAcAABBTaltlqbgDAAChIbhrQ2oPp6BVFgAAIFbYDIuq2OMOAACEiOCuDXE7bBxOAQAAEEMMq0XVpqlq2mUBAEAICO7aELfd0JEKgjsAAIBYYbNaJIl2WQAAEBKCuzYkzmFQcQcAABBDbNba5TYHVAAAgFAQ3LUhboehsspqVfEbXQAAgJjgr7irYn0GAACajuCuDYlzGJKk0orqKM8EAAAAkmQYx4K7GoI7AADQdAR3bYjbXhvccbIsAABAbDi+xx2tsgAAoOkI7toQX8VdCQdUAAAAxARaZQEAQHMQ3LUhbodNknSEAyoAAABigs3wHU5BcAcAAJqO4K4N8bXKllTQKgsAABALjGMVd94qWmUBAEDTEdy1Ib5WWSruAAAAYsPxPe6ouAMAAE1HcNeGOG1WWS0EdwAAALHCZqVVFgAAhI7grg2xWCyKc9g4nAIAACBG0CoLAACag+CujYlzGDpSzh53AAAAscBm1AZ3VNwBAIBQENy1MW6HoRJaZQEAAGKCwR53AACgGUIK7tauXRvWSSxatEi9evWSy+VSWlqaNm3a1OD4FStWqH///nK5XBo8eLDeeuutgOdN09SsWbPUrVs3ud1uZWRk6LPPPvM//8UXX2jSpEnq3bu33G63+vTpo5ycHHm93oD7fPjhh7rooovkcrnUo0cPzZ07N3wfuoW47QZ73AEAgKgK91qxNbPRKgsAAJohpOBu1KhR6tOnjx588EF99dVXzZrA8uXLlZ2drZycHG3dulVDhgxRZmam9u3bF3T8+vXrNW7cOE2aNEnbtm1TVlaWsrKy9PHHH/vHzJ07V48//rgWL16sjRs3Kj4+XpmZmSovL5ck7dixQzU1NXrqqaf0ySef6LHHHtPixYs1Y8YM/z08Ho+uuOIK9ezZU1u2bNHDDz+s2bNn6+mnn27W521pboehI+xxBwAAoiica8XWjsMpAABAc4QU3O3Zs0dTpkzRq6++qtNPP12ZmZl65ZVX6lSsNcajjz6qyZMna+LEiRo4cKAWL16suLg4LVmyJOj4BQsWaNSoUZo2bZoGDBigOXPmaNiwYVq4cKGk2mq7+fPna+bMmbr66qt19tln6/nnn9fevXu1atUqSbWLyWeffVZXXHGFTj/9dI0ePVp33XWXVq5c6X+fF198UV6vV0uWLNFZZ52l66+/XnfccYceffTRpn9hEeS2G/KUsccdAACInnCuFVs7WmUBAEBzhBTcJScn65e//KW2b9+ujRs36swzz9Stt96q7t2764477tAHH3zQqPt4vV5t2bJFGRkZxydktSojI0P5+flBX5Ofnx8wXpIyMzP943fv3q3CwsKAMUlJSUpLS6v3npJUXFyszp07B7zPxRdfLIfDEfA+O3fu1KFDh4Leo6KiQh6PJ+ARaW67wamyAAAgqsK1VmwLfK2ylbTKAgCAEDT7cIphw4Zp+vTpmjJlikpKSrRkyRINHz5cF110kT755JMGX3vgwAFVV1crJSUl4HpKSooKCwuDvqawsLDB8b7/NuWeu3bt0hNPPKFf/OIXJ32f777HiXJzc5WUlOR/9OjRI+i4llR7qizBHQAAiA3NWSu2BVarRVaLVEmrLAAACEHIwV1lZaVeffVV/fCHP1TPnj319ttva+HChSoqKtKuXbvUs2dPjRkzJpxzbRF79uzRqFGjNGbMGE2ePLlZ95o+fbqKi4v9j2js6eJ22FRSTqssAACIrrayVgwHm9WqyiqCOwAA0HS2UF50++2366WXXpJpmrrxxhs1d+5cDRo0yP98fHy8HnnkEXXv3r3B+yQnJ8swDBUVFQVcLyoqUmpqatDXpKamNjje99+ioiJ169YtYMzQoUMDXrd3715ddtllGjFiRJ1DJ+p7n+++x4mcTqecTmfQ5yIlzmGopKI6qnMAAADtW7jWim2FzbCoqoZWWQAA0HQhVdz95z//0RNPPKG9e/dq/vz5AQsxn+TkZK1du7bB+zgcDg0fPlx5eXn+azU1NcrLy1N6enrQ16SnpweMl6Q1a9b4x/fu3VupqakBYzwejzZu3Bhwzz179ujSSy/V8OHD9eyzz8pqDfwq0tPT9c9//lOVlcer19asWaN+/fqpU6dODX6uaHLbDXmra1RRRXgHAACiI1xrxbbCZrXIy+EUAAAgBCEFdzk5ORozZkyd6rKqqir985//lCTZbDZdcsklJ71Xdna2nnnmGS1dulSffvqpbrnlFpWWlmrixImSpPHjx2v69On+8VOnTtXq1as1b9487dixQ7Nnz9bmzZs1ZcoUSZLFYtGdd96pBx98UK+//ro++ugjjR8/Xt27d1dWVpak46Hd9773PT3yyCPav3+/CgsLA/auu+GGG+RwODRp0iR98sknWr58uRYsWKDs7OxQvrKIiXMYkqQS9rkDAABREs61YltQ2ypLxR0AAGi6kFplL7vsMn3zzTfq2rVrwPXi4mJddtllqq5ufLXX2LFjtX//fs2aNUuFhYUaOnSoVq9e7T8IoqCgIKAabsSIEVq2bJlmzpypGTNmqG/fvlq1alXAb3LvvvtulZaW6uabb9bhw4c1cuRIrV69Wi6XS1Jt5dyuXbu0a9cunXbaaQHzMc3aRVVSUpLeeecd3XbbbRo+fLiSk5M1a9Ys3XzzzU37siLMfSy4O1JepS4dotu2CwAA2qdwrhXbgtpWWSruAABA01lMX1LVBFarVUVFRTrllFMCrv/3v//VueeeK4/HE7YJtmYej0dJSUlas2234hMSIvKeuw+UasafP9Ibt4/UoFOTIvKeAAAgfHzrh+LiYiUmJkZ7OiFpD2vFpqzzsl/ZrtFDu2v6DwZEaHYAACAWhbLOa1LF3U9+8hNJte2oN910U0D7Q3V1tT788EONGDGiKbdEmLnttRV3Hk6WBQAAEdZSa8VFixbp4YcfVmFhoYYMGaInnnhC559/fr3jV6xYofvuu09ffPGF+vbtq9/97nf64Q9/GHTs//t//09PPfWUHnvsMd15551Nnltj2KwWWmUBAEBImhTcJSXVVnCZpqmEhAS53W7/cw6HQxdccIEmT54c3hmiSdjjDgAAREtLrBWXL1+u7OxsLV68WGlpaZo/f74yMzO1c+fOOq24krR+/XqNGzdOubm5+tGPfqRly5YpKytLW7durXNIxp///Gdt2LChxU+3tRlWWmUBAEBImhTcPfvss5KkXr166a677lJ8fHyLTAqh++4edwAAAJHUEmvFRx99VJMnT/YfXLZ48WK9+eabWrJkie6555464xcsWKBRo0Zp2rRpkqQ5c+ZozZo1WrhwoRYvXuwft2fPHt1+++16++23deWVVzZ7ng0xrFIlp8oCAIAQhHyqLKFdbLIbVtkNi47QKgsAAKIkXGtFr9erLVu2KCMjw3/NarUqIyND+fn5QV+Tn58fMF6SMjMzA8bX1NToxhtv1LRp03TWWWc1ai4VFRXyeDwBj8YyrFZVVtMqCwAAmq7RFXfDhg1TXl6eOnXqpHPOOUcWi6XesVu3bg3L5BCaeKdNHiruAABABLXEWvHAgQOqrq5WSkpKwPWUlBTt2LEj6GsKCwuDji8sLPT/+Xe/+51sNpvuuOOORs1DknJzc3X//fc3evx32awWKu4AAEBIGh3cXX311f4NhrOyslpqPgiDeIdNnjIq7gAAQOS0lrXili1btGDBAm3durXBcPFE06dPV3Z2tv/PHo9HPXr0aNRrDYI7AAAQokYHdzk5OUH/N2JPnMNgjzsAABBRLbFWTE5OlmEYKioqCrheVFSk1NTUoK9JTU1tcPx7772nffv26Xvf+57/+erqav3qV7/S/Pnz9cUXXwS9r9PpDDgltylqK+5olQUAAE0X0h53X331lb7++mv/nzdt2qQ777xTTz/9dNgmhtDFOQx52OMOAABESbjWig6HQ8OHD1deXp7/Wk1NjfLy8pSenh70Nenp6QHjJWnNmjX+8TfeeKM+/PBDbd++3f/o3r27pk2bprfffrtJ82ssw2pRZRUVdwAAoOlCCu5uuOEGrV27VlLtPiIZGRnatGmT7r33Xj3wwANhnSCaLs5hUzGtsgAAIErCuVbMzs7WM888o6VLl+rTTz/VLbfcotLSUv8ps+PHj9f06dP946dOnarVq1dr3rx52rFjh2bPnq3NmzdrypQpkqQuXbpo0KBBAQ+73a7U1FT169cvTN9AIJvVqsoagjsAANB0IQV3H3/8sc4//3xJ0iuvvKLBgwdr/fr1evHFF/Xcc8+Fc34IQZzDYI87AAAQNeFcK44dO1aPPPKIZs2apaFDh2r79u1avXq1/wCKgoICffPNN/7xI0aM0LJly/T0009ryJAhevXVV7Vq1SoNGjQobJ+vqWxWi7xU3AEAgBA0eo+776qsrPTv8fHuu+9q9OjRkqT+/fsHLJwQHZwqCwAAoinca8UpU6b4K+ZOtG7dujrXxowZozFjxjT6/vXtaxcuBnvcAQCAEIVUcXfWWWdp8eLFeu+997RmzRqNGjVKkrR371516dIlrBNE07mpuAMAAFHEWjGQzeBUWQAAEJqQgrvf/e53euqpp3TppZdq3LhxGjJkiCTp9ddf97dFIHrij50qa5r8ZhcAAEQea8VAhtVKcAcAAEISUqvspZdeqgMHDsjj8ahTp07+6zfffLPi4uLCNjmEJs5hU7Vp6qi3WvHOkH7EAAAAIWOtGMhGqywAAAhRyKmOYRgBCzFJ6tWrV3PngzCIdxqSJE95JcEdAACICtaKx9kMi6qouAMAACEIqVW2qKhIN954o7p37y6bzSbDMAIeiK44R21Y5ynjgAoAABB5rBUDcTgFAAAIVUjlWDfddJMKCgp03333qVu3brJYLOGeF5oh/lhwd6ScAyoAAEDksVYMZGOPOwAAEKKQgrt//etfeu+99zR06NAwTwfhEPedVlkAAIBIY60YqLbijuAOAAA0XUitsj169ODE0hgWT6ssAACIItaKgTicAgAAhCqk4G7+/Pm655579MUXX4R5OggHu2GRzbBQcQcAAKKCtWIgm2FRVQ0VdwAAoOlCapUdO3asjh49qj59+iguLk52uz3g+YMHD4ZlcgiNxWJRB4dNnjKCOwAAEHmsFQP5DqcwTbPd7/cHAACaJqTgbv78+WGeBsItzmHIU06rLAAAiDzWioFs1toml6oaU3aD4A4AADReSMHdhAkTwj0PhFmc06DiDgAARAVrxUA2a21YV1Vtym5EeTIAAKBVCWmPO0n6/PPPNXPmTI0bN0779u2TJP3tb3/TJ598ErbJIXRxdht73AEAgKhhrXicL7jzcrIsAABoopCCu3/84x8aPHiwNm7cqJUrV6qkpESS9MEHHygnJyesE0Ro3A5DxVTcAQCAKGCtGMgwfBV3BHcAAKBpQgru7rnnHj344INas2aNHA6H//rll1+uDRs2hG1yCF280yZPGXvcAQCAyGOtGMhXcVdZbUZ5JgAAoLUJKbj76KOP9OMf/7jO9a5du+rAgQPNnhSar/ZwCiruAABA5LFWDOQ7nKKSijsAANBEIQV3HTt21DfffFPn+rZt23Tqqac2e1JovniHTUdolQUAAFHAWjHQ8Yo7gjsAANA0IQV3119/vX7961+rsLBQFotFNTU1ev/993XXXXdp/Pjx4Z4jQhDnNOQpr5Jp0pIBAAAii7ViIINWWQAAEKKQgrvf/OY36t+/v3r06KGSkhINHDhQF110kUaMGKGZM2eGe44IQbzDpqoaU+WV/GYXAABEFmvFQDaDVlkAABAaWygvcjgceuaZZzRr1ix99NFHKikp0TnnnKO+ffuGe34IkdthSJI85ZX+/w0AABAJrBUD0SoLAABC1ejgLjs7u8Hnv3tC2KOPPhr6jBAW8Y7aH62nrFIpia4ozwYAALR1rBXrR6ssAAAIVaODu23btgX8eevWraqqqlK/fv0kSf/9739lGIaGDx8e3hkiJHHfqbgDAABoaawV6+eruKui4g4AADRRo4O7tWvX+v/3o48+qoSEBC1dulSdOnWSJB06dEgTJ07URRddFP5Zosninb6Ku6oozwQAALQHrBXr56u48xLcAQCAJgrpcIp58+YpNzfXvxCTpE6dOunBBx/UvHnzwjY5hI6KOwAAEC2sFQMdP5yCVlkAANA0IQV3Ho9H+/fvr3N9//79OnLkSLMnheZz2qwyrBZ5yqm4AwAAkcVaMRCtsgAAIFQhBXc//vGPNXHiRK1cuVJff/21vv76a7322muaNGmSfvKTn4R7jgiBxWJRvMOQp4yKOwAAEFmsFQPRKgsAAELV6D3uvmvx4sW66667dMMNN6iysjYYstlsmjRpkh5++OGwThChi3faaJUFAAARx1oxkM3wVdzRKgsAAJompOAuLi5Ov//97/Xwww/r888/lyT16dNH8fHxYZ0cmifOYXA4BQAAiDjWioEMS21wV0nFHQAAaKKQgjuf+Ph4nX322eGaC8LM7TCouAMAAFHDWrGWxWKRzWohuAMAAE0W0h53aB3iHDb2uAMAAIgBdsOqiiqCOwAA0DQEd21YvMNQMcEdAABA1NkNC4dTAACAJiO4a8OouAMAAIgNdsOqikqCOwAA0DQEd21YnMOQp5zDKQAAAKLNblipuAMAAE1GcNeGxTttKiG4AwAAiDq7YaHiDgAANBnBXRsW5zDkra5ReWV1tKcCAADQrtUeTsGaDAAANA3BXRsW77BJEvvcAQAARJnNsMjLqbIAAKCJCO7asA6u2uDuMMEdAABAVNVW3BHcAQCApiG4a8PinceCu6MEdwAAANFkN6xU3AEAgCYjuGvDOviDO2+UZwIAANC+2awW9rgDAABNRnDXhsU7DUm0ygIAAESb3UarLAAAaDqCuzbMZrXKbTdUTKssAABAVNmtFoI7AADQZAR3bVyCy6bDZbTKAgAARJPdsKq8klZZAADQNAR3bVy808bhFAAAAFHG4RQAACAUBHdtXLzTYI87AACAKLMbtMoCAICmI7hr4+IdNk6VBQAAiDK7zSpvNcEdAABoGoK7Nq4DrbIAAABRZ7da5WWPOwAA0EQEd21cgovgDgAAINrshlXeajPa0wAAAK0MwV0bF++0qZg97gAAAKKqdo87Ku4AAEDTENy1cR2cNpVUVKmSPVUAAACixm5YVVltqqaGqjsAANB4BHdtXAenTZLkoeoOAAAgauy22mU3B1QAAICmILhr43zB3WGCOwAAgKixWy2SpIoqgjsAANB4BHdtXLwvuOOACgAAgKixG8cq7gjuAABAExDctXEdXLXBXXGZN8ozAQAAaL9shq/ijgMqAABA4xHctXHxDiruAAAAos1xrOKOVlkAANAUBHdtnMNmldNmJbgDAACIIhutsgAAIAQEd+1Agsumw0dplQUAAIgWu8HhFAAAoOkI7tqBeKeNU2UBAACiyEHFHQAACAHBXTvQwWmjVRYAACCKbP497jicAgAANB7BXTsQ76BVFgAAIJp8rbJU3AEAgKYguGsH4p02HaLiDgAAIGrsnCoLAABCEPXgbtGiRerVq5dcLpfS0tK0adOmBsevWLFC/fv3l8vl0uDBg/XWW28FPG+apmbNmqVu3brJ7XYrIyNDn332WcCYhx56SCNGjFBcXJw6duwY9H0sFkudx8svv9yszxotCS6bDpdRcQcAABAtdlplAQBACKIa3C1fvlzZ2dnKycnR1q1bNWTIEGVmZmrfvn1Bx69fv17jxo3TpEmTtG3bNmVlZSkrK0sff/yxf8zcuXP1+OOPa/Hixdq4caPi4+OVmZmp8vJy/xiv16sxY8bolltuaXB+zz77rL755hv/IysrKyyfO9LinTYVU3EHAAAQNTZaZQEAQAiiGtw9+uijmjx5siZOnKiBAwdq8eLFiouL05IlS4KOX7BggUaNGqVp06ZpwIABmjNnjoYNG6aFCxdKqq22mz9/vmbOnKmrr75aZ599tp5//nnt3btXq1at8t/n/vvv1y9/+UsNHjy4wfl17NhRqamp/ofL5QrbZ4+kDk6bjpRXqbrGjPZUAAAA2iWrxSKbYaFVFgAANEnUgjuv16stW7YoIyPj+GSsVmVkZCg/Pz/oa/Lz8wPGS1JmZqZ//O7du1VYWBgwJikpSWlpafXesyG33XabkpOTdf7552vJkiUyzYaDr4qKCnk8noBHLOjgtMmUdKScqjsAAIBocRhWKu4AAECTRC24O3DggKqrq5WSkhJwPSUlRYWFhUFfU1hY2OB433+bcs/6PPDAA3rllVe0Zs0aXXPNNbr11lv1xBNPNPia3NxcJSUl+R89evRo0nu2lA5OQ5J0mHZZAACAqLEbViruAABAk9iiPYFYdd999/n/9znnnKPS0lI9/PDDuuOOO+p9zfTp05Wdne3/s8fjiYnwLt5Z+2M+XEZwBwAAEC12w6KKSg6nAAAAjRe1irvk5GQZhqGioqKA60VFRUpNTQ36mtTU1AbH+/7blHs2Vlpamr7++mtVVFTUO8bpdCoxMTHgEQs6+IK7o5wsCwAAEC12w6qKairuAABA40UtuHM4HBo+fLjy8vL812pqapSXl6f09PSgr0lPTw8YL0lr1qzxj+/du7dSU1MDxng8Hm3cuLHeezbW9u3b1alTJzmdzmbdJxo6uGqDu2Iq7gAAAKLGblhVUUlwBwAAGi+qp8pmZ2frmWee0dKlS/Xpp5/qlltuUWlpqSZOnChJGj9+vKZPn+4fP3XqVK1evVrz5s3Tjh07NHv2bG3evFlTpkyRJFksFt1555168MEH9frrr+ujjz7S+PHj1b17d2VlZfnvU1BQoO3bt6ugoEDV1dXavn27tm/frpKSEknSX//6V/3hD3/Qxx9/rF27dunJJ5/Ub37zG91+++2R+3LCyGFYZTcs7HEHAABapUWLFqlXr15yuVxKS0vTpk2bGhy/YsUK9e/fXy6XS4MHD9Zbb70V8Pzs2bPVv39/xcfHq1OnTsrIyNDGjRtb8iNIqm2V9VJxBwAAmiCqe9yNHTtW+/fv16xZs1RYWKihQ4dq9erV/sMlCgoKZLUezxZHjBihZcuWaebMmZoxY4b69u2rVatWadCgQf4xd999t0pLS3XzzTfr8OHDGjlypFavXi2Xy+UfM2vWLC1dutT/53POOUeStHbtWl166aWy2+1atGiRfvnLX8o0TZ1xxhl69NFHNXny5Jb+SlqExWJRgtNOcAcAAFqd5cuXKzs7W4sXL1ZaWprmz5+vzMxM7dy5U127dq0zfv369Ro3bpxyc3P1ox/9SMuWLVNWVpa2bt3qXzOeeeaZWrhwoU4//XSVlZXpscce0xVXXKFdu3bplFNOabHPYqPiDgAANJHFNE0z2pNoqzwej5KSkrRm227FJyREdS53v/aBMgakKOeqs6I6DwAA0DDf+qG4uDhm9suNprS0NJ133nlauHChpNqtVXr06KHbb79d99xzT53xY8eOVWlpqd544w3/tQsuuEBDhw7V4sWLg76H7zt/99139f3vf79R8wplnffQW/9R7+QOemLcOY0aDwAA2pZQ1nlRbZVF5HRw2lRMxR0AAGhFvF6vtmzZooyMDP81q9WqjIwM5efnB31Nfn5+wHhJyszMrHe81+vV008/raSkJA0ZMqTeuVRUVMjj8QQ8msputXKqLAAAaBKCu3Yi3mHjVFkAANCqHDhwQNXV1f5tVHxSUlJUWFgY9DWFhYWNGv/GG2+oQ4cOcrlceuyxx7RmzRolJyfXO5fc3FwlJSX5Hz169Gjy57EbVlVU0SoLAAAaj+CunYh32nSQijsAAABJ0mWXXabt27dr/fr1GjVqlK677jrt27ev3vHTp09XcXGx//HVV181+T1thoXgDgAANAnBXTuR4LLpYCkVdwAAoPVITk6WYRgqKioKuF5UVKTU1NSgr0lNTW3U+Pj4eJ1xxhm64IIL9Mc//lE2m01//OMf652L0+lUYmJiwKOpaivuaJUFAACNR3DXTiS67AR3AACgVXE4HBo+fLjy8vL812pqapSXl6f09PSgr0lPTw8YL0lr1qypd/x371tRUdH8STfAbljlpeIOAAA0gS3aE0BkJLptKqmoUkVVtZw2I9rTAQAAaJTs7GxNmDBB5557rs4//3zNnz9fpaWlmjhxoiRp/PjxOvXUU5WbmytJmjp1qi655BLNmzdPV155pV5++WVt3rxZTz/9tCSptLRUDz30kEaPHq1u3brpwIEDWrRokfbs2aMxY8a06GexGxZVVBLcAQCAxiO4aycSXHZJ0qHSSqUmEdwBAIDWYezYsdq/f79mzZqlwsJCDR06VKtXr/YfQFFQUCCr9XgTyYgRI7Rs2TLNnDlTM2bMUN++fbVq1SoNGjRIkmQYhnbs2KGlS5fqwIED6tKli8477zy99957Ouuss1r0s9gNqyqqaZUFAACNR3DXTiQeC+6+La1QapIryrMBAABovClTpmjKlClBn1u3bl2da2PGjKm3es7lcmnlypXhnF6j2Q0LrbIAAKBJ2OOunUh01Wa0h0o5WRYAACAa7IaVVlkAANAkBHftRKL7eMUdAAAAIs9uWOWtJrgDAACNR3DXTjhtVjkMKyfLAgAARAmtsgAAoKkI7toJi8WiRLeN4A4AACBK7IZVVTWmqmvMaE8FAAC0EgR37Uiiy65vCe4AAACiwm7ULr2pugMAAI1FcNeOJLhsOlhCcAcAABANvuCuoqo6yjMBAACtBcFdO5LgsnM4BQAAQJTYDIskKu4AAEDjEdy1I4kum76l4g4AACAqHP6KO4I7AADQOAR37UiC287hFAAAAFFiJ7gDAABNRHDXjiS67Couq+QkMwAAgCjwtcqyxx0AAGgsgrt2JNFlkynp0FGq7gAAACLNwamyAACgiQju2pFEt12SaJcFAACIguMVdwR3AACgcQju2pEEl02SOKACAAAgCjicAgAANBXBXTuS6KLiDgAAIFpstMoCAIAmIrhrR+IchmxWiw6WVkR7KgAAAO2OncMpAABAExHctSMWi0WJLru+peIOAAAg4jicAgAANBXBXTuT4LbRKgsAABAFhpXDKQAAQNMQ3LUzCS4bFXcAAABRYLFY5DCsqqikVRYAADQOwV07k+Cyc6osAABAlNgNi7zVVNwBAIDGIbhrZxJddn1bwuEUAAAA0WC3WVVRSXAHAAAah+CunUl02XTwKBV3AAAA0WC3Wqm4AwAAjUZw184kuOw6XFqpmhoz2lMBAABod+w2C4dTAACARiO4a2cS3TZVm6Y85ZXRngoAAEC7Yzes8hLcAQCARiK4a2cSXXZJ4mRZAACAKLAbFlVUcaosAABoHIK7dsYX3B0kuAMAAIg4u8HhFAAAoPEI7tqZBLdNkvRtCcEdAABApNmsVlVwOAUAAGgkgrt2poPTJquFijsAAIBosBsWKu4AAECjEdy1M1aLRQkuu74tqYj2VAAAANqd2sMp2OMOAAA0DsFdO9TRbdd+gjsAAICIsxlWlXOqLAAAaCSCu3YoKc6ufR6COwAAgEhzGBZ5Ce4AAEAjEdy1Qx3ddhUdKY/2NAAAANodm2FVBa2yAACgkQju2qGOcQ4q7gAAAKLAblg5nAIAADQawV071CnOrv1HKmSaZrSnAgAA0K7YDYu81QR3AACgcQju2qGOcQ55q2vkKauK9lQAAADaFbthVQV73AEAgEYiuGuHOrrtkqT9JexzBwAAEEl2w8rhFAAAoNEI7tqhjnEOSWKfOwAAgAizGxYOpwAAAI1GcNcOdYyrrbjbd4TgDgAAIJKouAMAAE1BcNcOueyG3HZD+47QKgsAABBJdsOqGlOq5IAKAADQCAR37VSneDutsgAAABHmstUuv496aZcFAAAnR3DXTnV0O2iVBQAAiDCn3ZAklRHcAQCARiC4a6eS3HYVeWiVBQAAiCSXvXb5XeqtivJMAABAa0Bw1051jLNrPxV3AAAAEeW01VbcHa2g4g4AAJwcwV071THOQXAHAAAQYVTcAQCApiC4a6c6xdl1pKJK5ZX8thcAACBSXMf2uDtKcAcAABqB4K6d6hjnkCROlgUAAIgg17FW2VJaZQEAQCMQ3LVTHd12SdK+IxxQAQAAEClOW+3ym4o7AADQGAR37VQnX8Ud+9wBAABEjNVqkdNm1VEvFXcAAODkCO7aqXinIZth0T4PFXcAAACR5LIbBHcAAKBRCO7aKYvFok5uBxV3AAAAEeayW1VaQassAAA4OYK7dqxjnF37Ce4AAAAiymWj4g4AADQOwV07luS2U3EHAAAQYU4q7gAAQCMR3LVjHeMcKmKPOwAAgIii4g4AADQWwV071imOijsAAIBIo+IOAAA0FsFdO5YUZ9ehUq+qqmuiPRUAAIB2w2UzVOoluAMAACdHcNeOdXI7ZEo6UOKN9lQAAADaDafdSqssAABoFIK7dqxTvEOS2OcOAAAgglx2g1ZZAADQKAR37ViXY8HdN8VlUZ4JAABA++HkcAoAANBIBHftWILLJodh1Z7DVNwBAABEiotWWQAA0EgEd+2YxWJRcoJD3xym4g4AACBSXHZDR71VMk0z2lMBAAAxjuCunesS79ReWmUBAAAixmU3VGNKFVU10Z4KAACIcQR37VzneIe+PkRwBwAAECkuW+0SnHZZAABwMgR37VxyB4e+KWaPOwAAgEhx2g1J4mRZAABwUgR37VyXDk7tP1Khiip+4wsAABAJVNwBAIDGinpwt2jRIvXq1Usul0tpaWnatGlTg+NXrFih/v37y+VyafDgwXrrrbcCnjdNU7NmzVK3bt3kdruVkZGhzz77LGDMQw89pBEjRiguLk4dO3YM+j4FBQW68sorFRcXp65du2ratGmqqmp7vxXtEu+QJBUVV0R5JgAAAO2Dy1dx5217a0sAABBeUQ3uli9fruzsbOXk5Gjr1q0aMmSIMjMztW/fvqDj169fr3HjxmnSpEnatm2bsrKylJWVpY8//tg/Zu7cuXr88ce1ePFibdy4UfHx8crMzFR5+fF2UK/XqzFjxuiWW24J+j7V1dW68sor5fV6tX79ei1dulTPPfecZs2aFd4vIAYkd3BKEgdUAAAARIjLfqziroKKOwAA0LCoBnePPvqoJk+erIkTJ2rgwIFavHix4uLitGTJkqDjFyxYoFGjRmnatGkaMGCA5syZo2HDhmnhwoWSaqvt5s+fr5kzZ+rqq6/W2Wefreeff1579+7VqlWr/Pe5//779ctf/lKDBw8O+j7vvPOO/vOf/+hPf/qThg4dqh/84AeaM2eOFi1aJK/XG/bvIZq6dKituNt7mOAOAAAgEpxU3AEAgEaKWnDn9Xq1ZcsWZWRkHJ+M1aqMjAzl5+cHfU1+fn7AeEnKzMz0j9+9e7cKCwsDxiQlJSktLa3ee9b3PoMHD1ZKSkrA+3g8Hn3yySf1vq6iokIejyfgEeucNkOJLhsHVAAAAESIy1Yb3B0luAMAACcRteDuwIEDqq6uDgjHJCklJUWFhYVBX1NYWNjgeN9/m3LPprzPd98jmNzcXCUlJfkfPXr0aPR7RlOXDk7toeIOAAAgIuyGRVYLh1MAAICTi/rhFG3J9OnTVVxc7H989dVX0Z5So3SJd2jvIYI7AAAQm8J5mFllZaV+/etfa/DgwYqPj1f37t01fvx47d27t6U/hp/FYpHLbrDHHQAAOKmoBXfJyckyDENFRUUB14uKipSamhr0NampqQ2O9/23Kfdsyvt89z2CcTqdSkxMDHi0Bp3jHVTcAQCAmBTuw8yOHj2qrVu36r777tPWrVu1cuVK7dy5U6NHj47kx5LLbrDHHQAAOKmoBXcOh0PDhw9XXl6e/1pNTY3y8vKUnp4e9DXp6ekB4yVpzZo1/vG9e/dWampqwBiPx6ONGzfWe8/63uejjz4KWBCuWbNGiYmJGjhwYKPv01okd3Cyxx0AAIhJ4T7MLCkpSWvWrNF1112nfv366YILLtDChQu1ZcsWFRQUROxzuexWWmUBAMBJRbVVNjs7W88884yWLl2qTz/9VLfccotKS0s1ceJESdL48eM1ffp0//ipU6dq9erVmjdvnnbs2KHZs2dr8+bNmjJliqTatoM777xTDz74oF5//XV99NFHGj9+vLp3766srCz/fQoKCrR9+3YVFBSourpa27dv1/bt21VSUiJJuuKKKzRw4EDdeOON+uCDD/T2229r5syZuu222+R0OiP3BUVIcgeHSiqq5CmvjPZUAAAA/FriMLNgiouLZbFY1LFjx3rHhPsQMpfNUGkFFXcAAKBhtmi++dixY7V//37NmjVLhYWFGjp0qFavXu0/CKKgoEBW6/FsccSIEVq2bJlmzpypGTNmqG/fvlq1apUGDRrkH3P33XertLRUN998sw4fPqyRI0dq9erVcrlc/jGzZs3S0qVL/X8+55xzJElr167VpZdeKsMw9MYbb+iWW25Renq64uPjNWHCBD3wwAMt/ZVERZcOtWHkN4fLlZhqj/JsAAAAajV0mNmOHTuCvuZkh5mdqLy8XL/+9a81bty4Brc5yc3N1f3339/ET1A/JxV3AACgEaIa3EnSlClT/BVzJ1q3bl2da2PGjNGYMWPqvZ/FYtEDDzzQYMj23HPP6bnnnmtwXj179gzYyLgt6xLvkCTtPVymfqkJUZ4NAABAZFRWVuq6666TaZp68sknGxw7ffp0ZWdn+//s8XjUo0ePkN+bijsAANAYUQ/uEH2d4hyyWsQBFQAAIKa0xGFmPr7Q7ssvv9Tf//73kx4q5nQ6w7plisNm5XAKAABwUlHd4w6xwWq1HDugguAOAADEjpY4zEw6Htp99tlnevfdd9WlS5eW+QANcNkNWmUBAMBJUXEHSVLneIf2HuZkWQAAEFuys7M1YcIEnXvuuTr//PM1f/78OoeZnXrqqcrNzZVUe5jZJZdconnz5unKK6/Uyy+/rM2bN+vpp5+WVBvaXXvttdq6daveeOMNVVdX+/e/69y5sxwOR0Q+l8tu8EtTAABwUgR3kFS7z93Xh45GexoAAAABwn2Y2Z49e/T6669LkoYOHRrwXr6DyiLBxeEUAACgEQjuIKn2ZNktXx6K9jQAAADqCOdhZr169ZJpmuGcXkhcNkNHOZwCAACcBHvcQZLUNbF2jztvVU20pwIAANDmUXEHAAAag+AOkqTURJdqTNEuCwAAEAFOu6HyqhpV10S/+g8AAMQugjtIqg3uJOnLgwR3AAAALc1lq12GH/XSLgsAAOpHcAdJUqd4h+yGRV8eKI32VAAAANo8p92QJJXRLgsAABpAcAdJktViUUqiS198S8UdAABAS3MdC+5KCe4AAEADCO7gl5Lg0pffUnEHAADQ0nytsqWcLAsAABpAcAe/lEQnFXcAAAAR4Ku442RZAADQEII7+KUkuvTVwaOcbgYAANDCjrfKUnEHAADqR3AHv5REl6pqTO09XBbtqQAAALRpLvuxU2UrqLgDAAD1I7iDX2qSS5JUcJB2WQAAgJbktFFxBwAATo7gDn7JHZwyrBZ9wQEVAAAALcqwWmQ3LCpjjzsAANAAgjv4GVaLTung1JccUAEAANDi3HaDijsAANAggjsESEl06osDVNwBAAC0NJfdYI87AADQIII7BEhJdNEqCwAAEAFOu5WKOwAA0CCCOwRISXSp4NujMk0z2lMBAABo01w2Q6UVBHcAAKB+BHcIkJLoUnlVjfYdqYj2VAAAANq0OKeh4rLKaE8DAADEMII7BEhNdEkS+9wBAAC0sA5Ouw6WeqM9DQAAEMMI7hDglASnLJK+PMjJsgAAAC0pwWXToVIq7gAAQP0I7hDAYbOqSwcHFXcAAAAtLMFp08GjVNwBAID6Edyhjm5Jbn2+vyTa0wAAAGjTElw2ecoqORQMAADUi+AOdZzWya2dhUeiPQ0AAIA2rYPTrqoaU0c4WRYAANSD4A51nNYpTgUHj6q8sjraUwEAAGizElw2SdIhDqgAAAD1ILhDHad1cqvGFO2yAAAALcgf3B3lgAoAABAcwR3qOK2TW5L0WRHBHQAAQEvp4PQFd1TcAQCA4AjuUEecw6bkDg79t4h97gAAAFpKgssuiVZZAABQP4I7BHVqR7d2EtwBAAC0GIfNKqfNSqssAACoF8EdgjqtU5z+y8myAAAALSrBZaPiDgAA1IvgDkGd1smtrw+VqczLybIAAAAtJcFlZ487AABQL4I7BHVapziZknbt44AKAACAltLBadNhWmUBAEA9CO4QlO9kWfa5AwAAaDkdXDZ9S6ssAACoB8EdgnLZDXVNcOozgjsAAIAWk+BkjzsAAFA/gjvU69SObv2X4A4AAKDFdHDZ2OMOAADUi+AO9Tqtk5tWWQAAgBaU4LTr8NFKmaYZ7akAAIAYRHCHep3WKU57D5erpKIq2lMBAABokxJcNnmra1RWWR3tqQAAgBhEcId6+Q6oYJ87AACAltHBaZMkHWSfOwAAEATBHep1Wqc4GVaLPtnrifZUAAAA2qQEV21wd/hoZZRnAgAAYhHBHerlsFn1vc5uffj14WhPBQAAoE3yBXccUAEAAIIhuEODeid30AdfF0d7GgAAAG1SgssuiVZZAAAQHMEdGnR6crx2FZWozMuGyQAAAOHmtFllMyy0ygIAgKAI7tCg00/poGrT1H++oeoOAAAg3CwWixKddiruAABAUAR3aFCPTm7ZDYs+pF0WAACgRSS4bDrMHncAACAIgjs0yGb8//buPL6pKv8f/+tmT5qm+05bWiil7HspIDjSAQQdcRxFYJRRBkYFlx8KAqPAqJ8fOsqMy6i4ghvCMAKKYscCAiOUsstWKkuhFLoAXdK9Wc73j7SRQIECTW+avp4P8qC59+Te9z25bd5533vPVSA2yIeFOyIiIiI3MepUKOGlskRERNQIFu7omuKDffDz6VK5wyAiIiLySkatipfKEhERUaNYuKNrig/xQc75SpTX8EgwERERUXMzalUo4aWyRERE1AgW7uia4oONEAAOnjHLHQoRERGR1/HVsXBHREREjWPhjq4pyl8PnVqBA2dK5Q6FiIiIyOv46tQoqeSVDURERHQ5Fu7omhQKCXHBvEEFERERkTsYtSpUW2yosdjkDoWIiIg8DAt31CRxQbxBBREREZE7GHUqAEAp7yxLREREl2DhjpqkY6gvTpdUo8hcI3coRERERF7FVF+44zh3REREdCkW7qhJkiJ8AQDbc4pljoSIiIjIu/jpNQCAQh4gJSIiokuwcEdN4m/QoF2AHttPXJA7FCIiIiKvEuijgUICzpaycEdERESuWLijJuscbkLGcRbuiIiIiJqTUiEh0EeDM6VVcodCREREHoaFO2qyLhEm5Jyv5Dh3RERERM0s2KjFmZJqucMgIiIiD8PCHTUZx7kjIiIico8goxZ5LNwRERHRJVi4oybjOHdERERE7hFs1OBMKQt3RERE5IqFO7ouncNN2HbsvNxhEBEREXmVYKMWReZaWG12uUMhIiIiD8LCHV2XLhEmnLxQhUKOc0dERETUbIKNWtiEQAFzLCIiIroIC3d0XZzj3PFyWSIiIqJmE2LUAgBvUEFEREQuWLij68Jx7oiIiIiaX5BRAwA4W8bCHREREf2KhTu6bt2i/LAhqwhCCLlDISIiIvIKOrUSJp2KZ9wRERGRCxbu6Lr1iw1AUXktDpwpkzsUIiIiIq8RbNTyzrJERETkgoU7um6J4b4walVIP1wodyhEREREXiPIqOEZd0REROSChTu6biqFAj2j/fHDIRbuiIiIiJpLkFGLPBbuiIiI6CIs3NEN6RcbgOzCcpwurpI7FCIiIiKvEGLU4mxpNccRJiIiIicW7uiG9GznD7VS4uWyRERERM0k2KhFjdWO4so6uUMhIiIiD+ERhbu3334b7du3h06nQ3JyMnbs2HHV9itXrkTnzp2h0+nQvXt3rFu3zmW+EALz5s1DREQE9Ho9UlNTcfToUZc2xcXFmDhxIkwmE/z9/TF58mRUVFQ45588eRKSJF322L59e/NteCum1yjRJcKEH1i4IyIiImoWQUYNAOBsaY3MkRAREZGnkL1wt2LFCsyYMQPz58/Hnj170LNnT4wcORJFRUWNtt+2bRvGjx+PyZMnY+/evRg7dizGjh2LgwcPOtv8/e9/x5tvvonFixcjMzMTPj4+GDlyJGpqfk2CJk6ciEOHDiE9PR3ffvsttmzZgqlTp162vvXr1yM/P9/56Nu3b/N3QivVNzYAO3OKUVZlkTsUIiIiolYvxKgFAJwp5VAkRERE5CB74e4f//gHpkyZgoceeghdunTB4sWLYTAY8PHHHzfa/o033sCoUaMwc+ZMJCUl4cUXX0SfPn3wr3/9C4DjbLvXX38dzz33HO666y706NEDn376Kc6ePYs1a9YAALKyspCWloYPP/wQycnJGDJkCN566y0sX74cZ8+edVlfUFAQwsPDnQ+1Wu3W/mhN+sYGwiYE0rN41h0RERHRzfLVqaBVKXiDCiIiInKStXBXV1eH3bt3IzU11TlNoVAgNTUVGRkZjb4mIyPDpT0AjBw50tk+JycHBQUFLm38/PyQnJzsbJORkQF/f3/069fP2SY1NRUKhQKZmZkuy/7d736H0NBQDBkyBN98881Vt6e2thZms9nl4c0CfTToGmnCyl2n5Q6FiIiIvFhzD6uyatUqjBgxAkFBQZAkCfv27XNj9E0nSRKCjVqcKWXhjoiIiBxkLdydP38eNpsNYWFhLtPDwsJQUFDQ6GsKCgqu2r7h/2u1CQ0NdZmvUqkQGBjobGM0GrFo0SKsXLkS3333HYYMGYKxY8detXi3cOFC+Pn5OR/R0dHX6oJWb2hCCDJzipF7gZd0EBERUfNzx7AqlZWVGDJkCF555ZWW2owmCzJqcJaFOyIiIqon+6Wynio4OBgzZsxAcnIy+vfvj5dffhl//OMf8eqrr17xNXPmzEFZWZnzcfq095+JNiAuEHq1Ev/Zkyd3KEREROSFmntYFQB44IEHMG/evMuu4vAEwUYtcot5QJSIiIgcZC3cBQcHQ6lUorDQdYy0wsJChIeHN/qa8PDwq7Zv+P9abS49Smu1WlFcXHzF9QJAcnIyjh07dsX5Wq0WJpPJ5eHtdGolBsYH4T+7TsNuF3KHQ0RERF7EHcOq3KiWGhIlyl+PE+cqYbXZ3bJ8IiIial1kLdxpNBr07dsXGzZscE6z2+3YsGEDUlJSGn1NSkqKS3sASE9Pd7aPi4tDeHi4Sxuz2YzMzExnm5SUFJSWlmL37t3ONhs3boTdbkdycvIV4923bx8iIiKuf0O93K2JIThbVoNtxy/IHQoRERF5EXcMq3KjWmpIlJhAA2qtdpzkMCREREQEQCV3ADNmzMCkSZPQr18/DBgwAK+//joqKyvx0EMPAQAefPBBREVFYeHChQCAJ598EsOGDcOiRYswZswYLF++HLt27cL7778PwDGo71NPPYWXXnoJCQkJiIuLw/PPP4/IyEiMHTsWAJCUlIRRo0ZhypQpWLx4MSwWC6ZPn477778fkZGRAIBPPvkEGo0GvXv3BuAYxPjjjz/Ghx9+2MI95PkSQo2I9Nfj37tyMSQhWO5wiIiIiJrdnDlzMGPGDOdzs9nsluJdTKABAHCkwIyOocZmXz4RERG1LrIX7saNG4dz585h3rx5KCgoQK9evZCWluY8UpqbmwuF4tcTAwcNGoRly5bhueeew9y5c5GQkIA1a9agW7duzjazZs1CZWUlpk6ditLSUgwZMgRpaWnQ6XTONl988QWmT5+O4cOHQ6FQ4J577sGbb77pEtuLL76IU6dOQaVSoXPnzlixYgX+8Ic/uLlHWh9JkjAsIRhf7TmD4so6BPpo5A6JiIiIvIA7hlW5UVqtFlqt9qaW0RQmvRqBBjWO5Jfjjh5uXx0RERF5OEkIwYHJ3MRsNsPPzw/pe3Pg4+srdzhuZa6x4Ikv9+IvQ+MxY0Si3OEQERG1Wg35Q1lZWZsYL/dakpOTMWDAALz11lsAHMOqxMTEYPr06Zg9e/Zl7ceNG4eqqiqsXbvWOW3QoEHo0aMHFi9e7NL25MmTiIuLw969e9GrV6/risuded7L32ch2FeLjyb1b9blEhERkbxuJM+T/Yw78g4mnRq/6RyKpdtOYuqwDjBquWsRERHRzWvuYVUAoLi4GLm5uTh79iwAIDs7G4DjbL2bPTOvOUQHGrAnt0TuMIiIiMgDyHpzCvIud3SPQFWdDcsyT8kdChEREXmJcePG4bXXXsO8efPQq1cv7Nu377JhVfLz853tG4ZVef/999GzZ0/85z//uWxYlW+++Qa9e/fGmDFjAAD3338/evfufdkZeXKJCTTgbGkNzDUWuUMhIiIimfFSWTdqS5fKNli8+TgO55vx07O/gVallDscIiKiVoeXyrYO7szzTl2oxOxVB7DykRT0bx/YrMsmIiIi+dxInscz7qhZ/a5nJM6X1+Kr3WfkDoWIiIioVYry10OpkHAk3yx3KERERCQzFu6oWUX665EcH4h/bTyK6jqb3OEQERERtToqpQJR/npkFZTLHQoRERHJjIU7anbj+sXgXEUt3ttyXO5QiIiIiFql6EADsnjGHRERUZvHwh01u3A/HW7vFoF3Nx1HXkmV3OEQERERtToxgQZkF5TDbudw1ERERG0ZC3fkFmN7RcGgUeL/X5cldyhERERErU5MoAFVdTbklVTLHQoRERHJiIU7cgu9RonxA2Kw7kABth07L3c4RERERK1KTKABAHCYl8sSERG1aSzckdsM7hiMpAhfPPOfn2GuscgdDhEREVGrEWBQI8Cgxs95pXKHQkRERDJi4Y7cRiFJeHRYB5RWWTD/60Nyh0NERETUakiShM4RJmw7zisXiIiI2jIW7sitQnx1+NOg9li99wzW/nxW7nCIiIiIWo0uESYczDOjotYqdyhEREQkExbuyO2GdAxGSnwQ5q4+gNPFvMssERERUVN0jTDBJgR2nSyWOxQiIiKSCQt35HaSJOHhIXHw0ajw5092oZJHjYmIiIiuKdxPh0CDGhknLsgdChEREcmEhTtqEUatCjN+2wm5xVV4+t/7YLcLuUMiIiIi8mgN49xlHGfhjoiIqK1i4Y5aTHSgAY/d2gFphwrxxoajcodDRERE5PG6RJpw6IwZ5TUWuUMhIiIiGbBwRy2qX/tA3NcvGm9sOIqVu07LHQ4RERGRR+viHOeuRO5QiIiISAYs3FGLG9srErd1DsXsVQew+ZdzcodDRERE5LHCTToE+WiwnePcERERtUks3FGLkyQJDw+OQ892fnjks904kFcmd0hEREREHqlhnLttHOeOiIioTWLhjmShVEh4/LYEtAvQY9KSHThxrkLukIiIiIg8UtdIEw6dLcOFilq5QyEiIqIWxsIdyUanVuKZkYnQq5X440eZKDTXyB0SERERkcfpExMAAPjhcKHMkRAREVFLY+GOZGXSqTHn9s6os9rxwEeZKKviHdOIiIiILuanV6NLhAnrDuTLHQoRERG1MBbuSHZBRi1m356E/LIaTP5kJ2osNrlDIiIiIvIoA+ICse3YBZRU1skdChEREbUgFu7II0T56zFrZCIOnCnD9GV7YLXZ5Q6JiIiIyGP0bx8IuxBI5+WyREREbQoLd+QxOob64qnUBGw8UoS/rjkIIYTcIRERERF5BH+DBkkRJnzHy2WJiIjaFBbuyKP0ig7A1KEdsGLnafxr4zG5wyEiIiLyGAPiArH12HmOCUxERNSGsHBHHmdYpxDc27cdFqX/gtV78+QOh4iIiMgj9G8fCJtd4IfDBXKHQkRERC2EhTvySHf3jsKtiSGYuXI/th0/L3c4RERERLIL9NGgc4QvVu05I3coRERE1EJYuCOPJEkSJg+JQ5cIEx75bDdOnKuQOyQiIiIi2f0mMRQZJy4wNyIiImojWLgjj6VSKPDE8AT46tR4aOlOlFTWyR0SERERkayS44Lgq1NhWWau3KEQERFRC2Dhjjyaj1aFmSMTUVxZh0c+3406q13ukIiIiIhko1EpMKxTCFbuzkONxSZ3OERERORmLNyRxwsz6TAjtRN2nyrB/G8OQQghd0hEREREsrmtcyjKqi1YdyBf7lCIiIjIzVi4o1ahc4QJDw+Jw5c7cvFpxim5wyEiIiKSTYSfHt2j/PDZduZERERE3o6FO2o1fpMYitHdwvHC2sP46SjvNEtERERtV2pSGPbmluLgmTK5QyEiIiI3YuGOWpUJybHoFmXCY1/sRs75SrnDISIiIpJF39gAhJt0eGvjUblDISIiIjdi4Y5aFaVCwuO3Oe40+/DSnSirtsgdEhEREVGLUyok/K5XJP57qBBHCsxyh0NERERuwsIdtTo+WhWeHtEJ58prMX3ZHlhtvNMsERERtT23JAQjxFeLf208JncoRERE5CYs3FGrFOGnx5PDE7D12Hm89F2W3OEQERERtTiVQoHf9YzEd/vzcayoQu5wiIiIyA1YuKNWq1uUHx4aHIel205iydYcucMhIiIianHDOoUg0EeDtzZwrDsiIiJvxMIdtWqpSWEY0z0CL357GOsPF8odDhEREVGLUisVuLt3FL7++Sz2nS6VOxwiIiJqZizcUas3ITkGfWMDMP3LPTiQVyZ3OEREREQt6jeJoWgfZMD8bw7Cbhdyh0NERETNiIU7avUUkoRpv+mI6AADJi3ZgRPnOMYLERERtR0KhYRJKe3x8+kyrNp7Ru5wiIiIqBmxcEdeQatSYubIRBg0Svzxo0wUlNXIHRIRERFRi+kcYUJKfBBe/j4LFbVWucMhIiKiZsLCHXkNX50as0d1Rp3Vjgc+ysSFilq5QyIiIiJqMROTY1BeY8XCdVlyh0JERETNhIU78ipBRi1m356Ec+W1GP/Bdpxn8Y6IiIjaiCCjFhOTY/BFZi42HuFNu4iIiLwBC3fkdaL89XhuTBcUmWsx/v3tOFfO4h0RERG1DalJYegd7Y+ZK/fzACYREZEXYOGOvFJUgB7P3dEF5ytqcd97GThdXCV3SERERERuJ0kSpg6Nh8Vmx7P/2c+7zBIREbVyLNyR14ry12PeHV1RXWfD2He2Yn9eqdwhEREREbmdv0GDqUM7YOORIrz6Q7bc4RAREdFNYOGOvFq4nw4LftcVgQYN7nsvA/89VCB3SERERERu1zc2ABOTY/HupuP4fPspucMhIiKiG8TCHXk9P70afx2ThB7t/PGXz3Zj4bosWGx2ucMiIiIicqvR3cMxqms45n19EGkHefCSiIioNWLhjtoErUqJp4Yn4I/Jsfjgfycw/v3tyCvhuHdERETkvSRJwgMDYzEgLhCPfbEbS7bmyB0SERERXScW7qjNkCQJY3pE4Pk7uuDkhUqM+OcWfLb9FAdtJiIiIq+lUEh4/DcJuL1bBP629jDmfX0QtVab3GERERFRE7FwR21O53ATXrmnB1Lig/D8moMY/8F2ZOWb5Q6LiIiIyC0UCgl/HBiLPw+JwxeZuRj1+v+w7dh5ucMiIiKiJmDhjtokg0aFP98Sj7mjk3C6pBpj3vwf5q4+gPMVtXKHRkREROQWw5PCsPDu7tCpFJjwYSYe+Xw39p0ulTssIiIiugpJCMHrBN3EbDbDz88P6Xtz4OPrK3c4dAVWux3phwvx1Z482OwCkwa1x9Rb4hFk1ModGhERtUEN+UNZWRlMJpPc4dAVtOY8TwiBLUfP4+t9Z5BfVoN+sQG4f0AMRnQNg0mnljs8IiIir3UjeR4Ld27UmhO6tqiixorvDuTjv4ccd10b1z8ak4fEITrQIHNkRETUlrBw1zp4Q55ntwvsPlWCtEMFOJxvhlop4ZaOwRjUMRgD44OQFGGCUiHJHSYREZHXuJE8T+XmmIhaDaNOhXH9ozG6ezi+P1iAr3bn4dOMkxjZNRyTBrVHclwgJInJKxEREXkHhUJC/7hA9I8LxIWKWmTmFGNPbgleSTsCi01Ap1Kgc4QJ3aP80DvGH31iAhAbZGA+RERE1IJ4xp0becOR2Las1mrDll/OIe1QIc6WVqNjqBETk2MwtlcUAnw0codHREReimfctQ7enOfVWe04fq4CJ85VIudCJU6er8SZ0moAQISfDnf0iMCdPSPRPcqPRTwiIqLrwEtlPYw3J3RtiRACh86akZ5ViN2nSqCQgJFdw/GHvu0wpGMwVEre44WIiJoPC3etQ1vL8ypqrDhaVI69p0uxI6cYZdUW9Ir2x//3204YmhDMAh4REVET8FJZIjeQJAndovzQLcoPpVV1+OnYeWz+5Ry+3Z+PYKMGd/WKwp09I9GzHY86ExERkXcy6lToHROA3jEBmJTSHj/nlWLNvjOY9PEO9Inxxwt3dUO3KD+5wyQiIvI6POPOjdrakdi2RAiBnPOV+N+x88g4fgFl1Ra0C9BjTI8IjOwajl7t/KHgYM5ERHQDeMZd68A8z5EP7c8rw7Idp5BXUo1Jg9pjxm87wZd3piUiImoUz7gjaiGSJCE+xIj4ECP+mByLrHwzMk5cwPIdp/He5hMI8dXiN4khGNopBIM7BHNMPCIiIvI6kiShZ7Q/ukaZ8P2BAizLzMW6A/l44a5uGNk1XO7wiIiIvAILd0Q3San49VLayYMFfiksx85TJdh2/AL+vSsPEoCOoUb0ax+AXtH+SAw3oVOYEQZN8/76CSFQZ7NDCEAIQJIAjVLBM/+IiIjIrVQKBe7sGYmB8UFYui0Hf/lsN36bFIY5ozsjPsQod3hEREStGgt3RM1IoZDQOcKEzhEmALG4UFGLg2fNOFpYjq3HHGfkCQASgBBfLSL8dYjy18NPr4avTg2DRgmlJEGhkGC3C1hsdtTa7KiqtaGyzorKWivKaxyPilorquqsqKq1ocZqg8XW+FXvaqUEg0YFk04FP70aIb5ahJl0CPfTISbQgNggA+KDjTwrkIiIiG5KiK8Wz4xIxI6Txfgs4xR++48t+EPfdph+W0dEBxrkDo+IiKhVYuGOyI2CjFoM6xSCYZ1CAAC1VhvOlFTjdEkVisprcaGiDqeLq5FdV46qOhtqLXbYhYBdCCgkCSqlBLVSAa1KAZ1aCa1KAb1GiRBfLaIDDdCrFdCqHNNVSgVUCgmS5Lh0RQgBi03AarOj2mJDVZ0NFbVWlFVZkFtcjAsVdSittjhjDTZqkBjui26Rfujezg892/mjXYCeN9wgIiKiJpMkCclxQegdHYANRwrx9b6zWLHrNPrFBuCu3lFIiQ9CfLAPrwggIiJqIhbuiFqQVqV0jo3nCWosNhSV1+JsqaOYeLq4Cqv2nMF7W04AcBTz+rUPxID2gUjpEITEMF8m2kRERHRNGpUCt3eLwG8SQ7HzZDG2HT+P+V8fhF0ABo0SncJ8ERWgR7hJh1BfLULqH9EBBkQF6KFWKuTeBCIiIo/Awh1RG6ZTKxETaEBMoAEDEeScXlZtwfGiCmQXluNoUTnWZxXCahPwN6iREh+EwR2DMaRjMGKDDDwjj4iIiK5Ip1biloQQ3JIQgspaK3LOV+LEuQrklVTj1PlK7M0tQWmVBVV1NudrFBIQE2hAz2h/dI/yQ//2gegaaYKKxTwiImqDWLgjosv46dXoExuAPrEBAIA6qx1Hi8px+KwZh86a8d9DBbALIMJPh1sSgjGoQzAGxgch3E8nc+RERETkqXy0KucNvS5VZ7WjpKoOReW1KDTXIK+kGln5Znx/oAB1Njt8NEr0jwvEkI6OvKNzOK8CICKitoGFOyK6Jo1Kga6Rfuga6Yd7AVTVWXEkvxwHz5Zh+4li/HtXHgAgNsiAAe0DHUW/mAB0CPHh0XEiIiK6Jo1KgTCTDmEmHbpfVNiz2uw4cb4Sh8+acTjfjL+nZaPOlgV/vRoD4gIxIC4QfWMD0CXSBK1KKeMWEBERuQcLd0R03QwalcsZeWXVFhzJN+NQvhm7ThXjqz15sAtAq1IgMcwXnSN8ERvkg/ZBPgj30yHEqEWQUQODRnnFS23tdoFqS8PddG2orLWiqs6Gqjoraix21FptsNkF7AIQQkCjUkCjVECnUcKkUzvuoGvUwqRX8XJeIiKiVkqlVKBTmC86hflibO8o1Fnt+KWwHFkFZhzJL8eP2UdgsQmolRKSIkzoXn9GX6cwIzqEGOFv0Mi9CURERDeFhTsiuml+ejWS44OQHO8YJ6+6zoac8xU4eaEKpy5UYvepEnx3IB+VtTaX10mA8265kgQIAdjsArVWO+ps9maJTadSINSkQ2yQAbFBBrQP8kFCmC8SQo2I8NOxqEdERNSKaFQKl8ttrTY7Tl6owtGicuScq8SWo+fw5Y5c2IWjvb9ejQh/HSL99Qjy0cBP7zi456NVwUejgo9WBV+dCqb66f56NUx6NZS8DJeIiDyERxTu3n77bbz66qsoKChAz5498dZbb2HAgAFXbL9y5Uo8//zzOHnyJBISEvDKK69g9OjRzvlCCMyfPx8ffPABSktLMXjwYLz77rtISEhwtikuLsbjjz+OtWvXQqFQ4J577sEbb7wBo/HXu33u378f06ZNw86dOxESEoLHH38cs2bNck8nEHkRvUaJLpF+6BLpOoZNeY0FJVUWlFVbYK62oMZicxbpGtJjpUKCWqmASilBp1JCp1ZCp1ZAp1ZCX1/kU9efXadUSGiou9nsAhabQK3Fhqo6xxl6pdUWFFfWobiyDkXlNfjf0fNYuSsPtVZHUdCoVaFzuC+SIkxIijChS6QJiWG+0Gt4qQ0RkSeRI1ek1kGlVKBjqBEdQ3/N4eusduSXVeNsaTXyy2ocuUBFHU5dqEJVrRWVdTZnDnIlPholTHo1jFoVjDpHkU+nVkCrUkKtlKBQSFApJCgkCZIkQakAVAoFVAoJWrUCBo0KPhol/Azq+mLhxUVDJXQqJcfoIyKiJpG9cLdixQrMmDEDixcvRnJyMl5//XWMHDkS2dnZCA0Nvaz9tm3bMH78eCxcuBB33HEHli1bhrFjx2LPnj3o1q0bAODvf/873nzzTXzyySeIi4vD888/j5EjR+Lw4cPQ6RyD50+cOBH5+flIT0+HxWLBQw89hKlTp2LZsmUAALPZjBEjRiA1NRWLFy/GgQMH8PDDD8Pf3x9Tp05tuQ4i8iK+OjV8dWq3LFulALQqRzEu6Crt7ELgfHkt8kqqcbqkCqeKq/BjdhG+yDwFu3DcyS42yAddIk3oHOaLhDBfdAozIibQwPH6iIhkIFeuSK2XRqVAbJAPYoN8rtrOVj8sR3Wd1XnQr7LWhoo6q/PnaoujyFdtcQzXYbEJWO122IVjWA/AkVs0PLfaBSw2u/M1Fpu4cpxKBRQKQFlf/BPi17aSJEEhOQqTaqUEjUoBnUoJrVoJH40SRq3KUQg0qBFg0CDIqEGwUVv/0CDQRwMfjYrFQSIiLyCJiz8hZJCcnIz+/fvjX//6FwDAbrcjOjoajz/+OGbPnn1Z+3HjxqGyshLffvutc9rAgQPRq1cvLF68GEIIREZG4umnn8YzzzwDACgrK0NYWBiWLl2K+++/H1lZWejSpQt27tyJfv36AQDS0tIwevRo5OXlITIyEu+++y7++te/oqCgABqNY2yM2bNnY82aNThy5EiTts1sNsPPzw/pe3Pg4+t7U/1ERO5VZ7U7CnkXqpBbXIXc4krklVSjvMYKAFApJLQL0CM+2AftAg1oF6BHpL8eob46hPo6xuwzalv/eHpCCNRY7DDXOM6KLK22oKz+LMmGh7nGgvIaK8prLKio/2JTVWdFXf3Zk1abgF0ICAAKSXKcRamQoFUpoVUroFcrHZcoaZUwaFSOsxm0Khi0SvhoVDBoGs60dJxhqVJIUCkVzrMrhXBcGlVns6POakeN1Y6aOsd4iFV1tvqYrKiotaKq9tfp1XU21FodZ1hYbQI2IWC3CygU9V+OFApoVApoVQoY6r8U+WhVMOnULpdRNTwczx3zTXp1/SXfLfP+11ntKK+xwFxjdXlvGs5mNde/T+YaKypq6r+A1o8P2fA+2ewCQggIASgU9e+TUoJG6egHvUYJvdrxfjh+rj/7tf5M2IYzY1X1Z74qJAl2IWCzO77E1lod66q11n/prWv44vvrz7X141Va6r/oCvtFX1rrz77VKB3viV7j2D98dY6zX0w6NUyNvC8NZ7f46tTwuco4mp6sIX8oKyuDyWSSOxzZyZErNgXzPGqKOqvd+blUWWtFRZ21/m+f42+kgID9khP/BBx/m4VwFAJtQsBqc/ydrLM2FAXtqKovMJbXWGGuscB+ybc6CY47+erUCqgUjiJhw7AkNiFgswnHZ0F9W6m+UNjwWahRKqBVK6Gq/4xQSPWvtQvYBGCzOz5LFJLjzEOVUoJerXR+juvVjs/9hlxACDi2x+74HLbaHfmCsn75OrXjs9dXq4K/jwaBBg0CfNQINmoR6KOBv17Ng6hNIITjPbLWv1eSBEiQLvrMbn2fi0Te5EbyPFnPuKurq8Pu3bsxZ84c5zSFQoHU1FRkZGQ0+pqMjAzMmDHDZdrIkSOxZs0aAEBOTg4KCgqQmprqnO/n54fk5GRkZGTg/vvvR0ZGBvz9/Z1FOwBITU2FQqFAZmYm7r77bmRkZGDo0KHOol3Del555RWUlJQgICDgsthqa2tRW1vrfF5WVgYA+GrHUWj1Vz/iR0SeQw8gMVCFxABfmGssOFNajcKyGpw4W4kTZ883+/oakmFAavgHAPWJ1q8axgFsIOB4LuqfCCGcR/3lIkmOImf9M6D+C4lN3mNEl2noc8cZDgDg+FLkWVG6hwRApZScZ3MAcN7kRa4+UEqOy84Uil/3ebuA40uljPuOor4gKdX/Mo7qEobn7ugCH6170yez2QwAkPnYqkeQK1dsDPM8kpMCgBaAVgn4KgHoAMdXOcffI7tdoLLOivJqK8rqD67V1NlQXVuLkspfzxCULvq7plTAZSw/IQSq7PL/7aW26dI811OW68zTJclZ4Hb9v2mFUFF/ULshd3cU51F/0LN5Nlwh1f9O1+d4jX2nuFq8F+cdwjnNNV45v29cfBD/Rl/fcIazJLm+l4Dj51s6huD5O7u49cZGN5LnyVq4O3/+PGw2G8LCwlymh4WFXfGstoKCgkbbFxQUOOc3TLtam0svrVCpVAgMDHRpExcXd9kyGuY1VrhbuHAh/va3v102ffFfRjS6LURERNR6vFP/aCnl5eXw8/O7dkMvJleu2BjmeURERN4tG8CHLbSu68nzZB/jzpvMmTPH5QhvaWkpYmNjkZub2+YT7+ZiNpsRHR2N06dP8/KhZsR+dQ/2q3uwX92D/dr8brRPhRAoLy9HZGSkG6Oj68U878bwb0vTsJ+ahv10beyjpmE/NQ37qWmup59uJM+TtXAXHBwMpVKJwsJCl+mFhYUIDw9v9DXh4eFXbd/wf2FhISIiIlza9OrVy9mmqKjIZRlWqxXFxcUuy2lsPRev41JarRZarfay6X5+ftzJm5nJZGKfugH71T3Yr+7BfnUP9mvzu5E+ZSHIQa5csTHM824O/7Y0DfupadhP18Y+ahr2U9Own5qmqf10vXmerKN7ajQa9O3bFxs2bHBOs9vt2LBhA1JSUhp9TUpKikt7AEhPT3e2j4uLQ3h4uEsbs9mMzMxMZ5uUlBSUlpZi9+7dzjYbN26E3W5HcnKys82WLVtgsVhc1pOYmNjoZbJERERE1LzkyhWJiIiIPIXst+WZMWMGPvjgA3zyySfIysrCo48+isrKSjz00EMAgAcffNBlQOInn3wSaWlpWLRoEY4cOYIFCxZg165dmD59OgDHYItPPfUUXnrpJXzzzTc4cOAAHnzwQURGRmLs2LEAgKSkJIwaNQpTpkzBjh07sHXrVkyfPh3333+/83TFCRMmQKPRYPLkyTh06BBWrFiBN95447LBjomIiIjIfeTIFYmIiIg8hexj3I0bNw7nzp3DvHnzUFBQgF69eiEtLc05YHBubi4Uil/ri4MGDcKyZcvw3HPPYe7cuUhISMCaNWvQrVs3Z5tZs2ahsrISU6dORWlpKYYMGYK0tDTodDpnmy+++ALTp0/H8OHDoVAocM899+DNN990zvfz88MPP/yAadOmoW/fvggODsa8efMwderUJm+bVqvF/PnzG72sgm4M+9Q92K/uwX51D/are7Bfmx/7tHnIlSteC9/fpmE/NQ37qWnYT9fGPmoa9lPTsJ+axt39JInruQctERERERERERERtQjZL5UlIiIiIiIiIiKiy7FwR0RERERERERE5IFYuCMiIiIiIiIiIvJALNwRERERERERERF5IBbu3OTtt99G+/btodPpkJycjB07dsgdksdasGABJElyeXTu3Nk5v6amBtOmTUNQUBCMRiPuueceFBYWuiwjNzcXY8aMgcFgQGhoKGbOnAmr1drSmyKrLVu24M4770RkZCQkScKaNWtc5gshMG/ePERERECv1yM1NRVHjx51aVNcXIyJEyfCZDLB398fkydPRkVFhUub/fv345ZbboFOp0N0dDT+/ve/u3vTZHWtfv3Tn/502f47atQolzbsV1cLFy5E//794evri9DQUIwdOxbZ2dkubZrr937Tpk3o06cPtFotOnbsiKVLl7p782TTlH699dZbL9tfH3nkEZc27FdX7777Lnr06AGTyQSTyYSUlBR8//33zvncV9sm5nmumiOX80YtlZu1di2Va7VmLZk7tWYtmQu1Zi2V27R21+qnFt2XBDW75cuXC41GIz7++GNx6NAhMWXKFOHv7y8KCwvlDs0jzZ8/X3Tt2lXk5+c7H+fOnXPOf+SRR0R0dLTYsGGD2LVrlxg4cKAYNGiQc77VahXdunUTqampYu/evWLdunUiODhYzJkzR47Nkc26devEX//6V7Fq1SoBQKxevdpl/ssvvyz8/PzEmjVrxM8//yx+97vfibi4OFFdXe1sM2rUKNGzZ0+xfft28b///U907NhRjB8/3jm/rKxMhIWFiYkTJ4qDBw+KL7/8Uuj1evHee++11Ga2uGv166RJk8SoUaNc9t/i4mKXNuxXVyNHjhRLliwRBw8eFPv27ROjR48WMTExoqKiwtmmOX7vT5w4IQwGg5gxY4Y4fPiweOutt4RSqRRpaWktur0tpSn9OmzYMDFlyhSX/bWsrMw5n/16uW+++UZ899134pdffhHZ2dli7ty5Qq1Wi4MHDwohuK+2RczzLnezuZy3aonczBu0RK7V2rVU7tTatVQu1Nq1RG7jDa7VTy25L7Fw5wYDBgwQ06ZNcz632WwiMjJSLFy4UMaoPNf8+fNFz549G51XWloq1Gq1WLlypXNaVlaWACAyMjKEEI4Pe4VCIQoKCpxt3n33XWEymURtba1bY/dUlyY9drtdhIeHi1dffdU5rbS0VGi1WvHll18KIYQ4fPiwACB27tzpbPP9998LSZLEmTNnhBBCvPPOOyIgIMClX5999lmRmJjo5i3yDFdKJu+6664rvob9em1FRUUCgNi8ebMQovl+72fNmiW6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+HHntL/85S9i5MiRLutOSkoSdrvdOe3ZZ58VSUlJQgghTp06JZRKpThz5oxLfMOHDxdz5swRQjgSLwBi3759V93OuXPnisTERJd1vf3228JoNAqbzSaEEOKf//yniI2Nvepymro+m80mfH19xdq1a53TAIjVq1e7tGss0YuNjRVWq9U57d577xXjxo0TQgiRlZUlAIidO3c65x89elQAcCZ6ixYtEp06dRJ1dXVXjfHiGJRKpcjLy3NO+/7774VCoRD5+flCCCE6dOggli1b5vK6F198UaSkpAghft1PXn/99auuqyn705133ikeeuihRl//2WefXfY+1tbWCr1eL/773/8KIRx9GBYW5izkEREReTvmc8znWjKfE8LRD88995zzeUZGhgAgPvroI+e0L7/8Uuh0OufzQYMGiSlTprgs59577xWjR48WQghhsVhEcHCw+PTTT53zx48f7+w3IVwLd03Zt4haM14qS0ROPXr0cHkeERGBoqKim1pOWFgYDAYD4uPjXaZdutyBAwdCkiTn85SUFBw9ehQ2mw0HDhyAzWZDp06dnGOHGI1GbN682eW0e41Gc9k2XCorKwspKSku6xo8eDAqKiqQl5d3XdvZ2PoKCwsxZcoUJCQkwM/PDyaTCRUVFVe8zONqunbtCqVS6Xx+8fuRnZ0NlUqFPn36OOd37NgRAQEBzuf33nsvqqurER8fjylTpmD16tXOS0iuJCYmBlFRUc7nKSkpsNvtyM7ORmVlJY4fP47Jkye7vA8vvfTSZZc/9OvX77q391KPPvooli9fjl69emHWrFnYtm2bc97PP/+MY8eOwdfX1xlHYGAgampqXGLp3r07x7UjIqI2hfkc87mWzucu3VcARw528bSamhqYzWYAjvdv8ODBLssYPHgwsrKyAAAqlQr33Xef8/LcyspKfP3115g4cWKj62/qvkXUWvHmFETkdOmAs5IkwW63A4BzkF5x0TglF4/PcaXlSJJ01eU2RUVFBZRKJXbv3u2S+ABwGQBYr9e7JHDu1tj6Jk2ahAsXLuCNN95AbGwstFotUlJSUFdXd93Lv9l+i46ORnZ2NtavX4/09HQ89thjePXVV7F58+YbGly4oqICAPDBBx8gOTnZZd6l74uPj89Vl9WU/en222/HqVOnsG7dOqSnp2P48OGYNm0aXnvtNVRUVKBv376NjrcSEhLS5DiIiIi8DfO568N87lfXm881uHRfudK069nuiRMnYtiwYSgqKkJ6ejr0ej1GjRrVaNum7ltErRULd0TUJA3FkPz8fPTu3RsAXAY2vlmZmZkuz7dv346EhAQolUr07t0bNpsNRUVFuOWWW25qPUlJSfjqq68ghHAmEVu3boWvry/atWt3U8tuWNY777yD0aNHA3DcQOH8+fMubdRqNWw2202tJzExEVarFXv37kXfvn0BAMeOHUNJSYlLO71ejzvvvBN33nknpk2bhs6dO+PAgQMuR3Yvlpubi7NnzyIyMhKA431QKBRITExEWFgYIiMjceLEiSse8Wyqpu5PISEhmDRpEiZNmoRbbrkFM2fOxGuvvYY+ffpgxYoVCA0NhclkuqlYiIiI2grmc03DfM69kpKSsHXrVkyaNMk5bevWrejSpYvz+aBBgxAdHY0VK1bg+++/x7333nvFQmVz7ltEnoiFOyJqEr1ej4EDB+Lll19GXFwcioqK8NxzzzXb8nNzczFjxgz85S9/wZ49e/DWW29h0aJFAIBOnTph4sSJePDBB7Fo0SL07t0b586dw4YNG9CjRw+MGTOmyet57LHH8Prrr+Pxxx/H9OnTkZ2djfnz52PGjBnOo9A3IyEhAZ999hn69esHs9mMmTNnQq/Xu7Rp3749NmzYgMGDB0Or1bpcDtFUnTt3RmpqKqZOnYp3330XarUaTz/9tMtR46VLl8JmsyE5ORkGgwGff/459Ho9YmNjr7hcnU6HSZMm4bXXXoPZbMYTTzyB++67D+Hh4QCAv/3tb3jiiSfg5+eHUaNGoba2Frt27UJJSQlmzJjR5Pibsj/NmzcPffv2RdeuXVFbW4tvv/0WSUlJABxHYV999VXcddddeOGFF9CuXTucOnUKq1atwqxZs5olaSciIvI2zOeahvmce82cORP33XcfevfujdTUVKxduxarVq3C+vXrXdpNmDABixcvxi+//IIff/zxistrzn2LyBNxjDsiarKPP/4YVqsVffv2xVNPPYWXXnqp2Zb94IMPorq6GgMGDMC0adPw5JNPYurUqc75S5YswYMPPoinn34aiYmJGDt2LHbu3ImYmJjrWk9UVBTWrVuHHTt2oGfPnnjkkUcwefLkZktaP/roI5SUlKBPnz544IEH8MQTTyA0NNSlzaJFi5Ceno7o6Gjn0e4b8emnnyIsLAxDhw7F3XffjSlTpsDX1xc6nQ4A4O/vjw8++ACDBw9Gjx49sH79eqxduxZBQUFXXGbHjh3x+9//HqNHj8aIESPQo0cPvPPOO875f/7zn/Hhhx9iyZIl6N69O4YNG4alS5ciLi7uuuO/1v6k0WgwZ84c9OjRA0OHDoVSqcTy5csBAAaDAVu2bEFMTAx+//vfIykpCZMnT0ZNTQ3PwCMiIroK5nPXxnzOvcaOHYs33ngDr732Grp27Yr33nsPS5Yswa233urSbuLEiTh8+DCioqIuGxPvUs21bxF5IklcPMABERG1Wnl5eYiOjsb69esxfPjw6379ggULsGbNmma9ZIaIiIiImo75HBFdipfKEhG1Uhs3bkRFRQW6d++O/Px8zJo1C+3bt8fQoUPlDo2IiIiImoD5HBFdCwt3REStlMViwdy5c3HixAn4+vpi0KBB+OKLL27oDmNERERE1PKYzxHRtfBSWSIiIiIiIiIiIg/Em1MQERERERERERF5IBbuiIiIiIiIiIiIPBALd0RERERERERERB6IhTsiIiIiIiIiIiIPxMIdERERERERERGRB2LhjoiIiIiIiIiIyAOxcEdEREREREREROSBWLgjIiIiIiIiIiLyQP8Ps5VJMyynj0oAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1500x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,8))\n",
    "plt.subplot(1,2,1)\n",
    "sns.kdeplot(n_ratings_per_user, fill=True)\n",
    "plt.xlim(0)\n",
    "plt.title(\"Number of Ratings Per User\", fontsize=14)\n",
    "plt.xlabel(\"number of ratings per user\")\n",
    "plt.ylabel(\"density\")\n",
    "plt.subplot(1,2,2)\n",
    "sns.kdeplot(n_ratings_per_movie, fill=True)\n",
    "plt.xlim(0)\n",
    "plt.title(\"Number of Ratings Per Movie\", fontsize= 14)\n",
    "plt.xlabel(\"number of ratings per movie\")\n",
    "plt.ylabel(\"density\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0b8ebc6",
   "metadata": {},
   "source": [
    "### Item based recommendation system using K-Nearest Neighbours\n",
    "Find the k movies that have the most similar user engagement vectors for movie i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "b100083a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting scikit-learn\n",
      "  Using cached scikit_learn-1.0.2-cp37-cp37m-macosx_10_13_x86_64.whl (7.8 MB)\n",
      "Requirement already satisfied: scipy>=1.1.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from scikit-learn) (1.7.3)\n",
      "Collecting threadpoolctl>=2.0.0\n",
      "  Using cached threadpoolctl-3.1.0-py3-none-any.whl (14 kB)\n",
      "Requirement already satisfied: numpy>=1.14.6 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from scikit-learn) (1.21.6)\n",
      "Collecting joblib>=0.11\n",
      "  Downloading joblib-1.3.2-py3-none-any.whl (302 kB)\n",
      "\u001b[K     |████████████████████████████████| 302 kB 726 kB/s eta 0:00:01\n",
      "\u001b[?25hInstalling collected packages: threadpoolctl, joblib, scikit-learn\n",
      "Successfully installed joblib-1.3.2 scikit-learn-1.0.2 threadpoolctl-3.1.0\n",
      "\u001b[33mWARNING: You are using pip version 20.1.1; however, version 24.0 is available.\n",
      "You should consider upgrading via the '/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7 -m pip install --upgrade pip' command.\u001b[0m\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install scikit-learn\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "fa0ee378",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import NearestNeighbors\n",
    "\n",
    "def find_similar_movies(movie_id, X, movie_mapper, movie_inv_mapper, k, metric='cosine'):\n",
    "    \"\"\"\n",
    "    Finds k-nearest neighbours for a given movie id.\n",
    "    \n",
    "    Args:\n",
    "        movie_id: id of the movie of interest\n",
    "        X: user-item utility matrix\n",
    "        k: number of similar movies to retrieve\n",
    "        metric: distance metric for kNN calculations\n",
    "    \n",
    "    Output: returns list of k similar movie ID's\n",
    "    \"\"\"\n",
    "    X = X.T\n",
    "    neighbour_ids = []\n",
    "    \n",
    "    movie_ind = movie_mapper[movie_id]\n",
    "    movie_vec = X[movie_ind]\n",
    "    if isinstance(movie_vec, (np.ndarray)):\n",
    "        movie_vec = movie_vec.reshape(1,-1)\n",
    "    # use k+1 since kNN output includes the movieId of interest\n",
    "    kNN = NearestNeighbors(n_neighbors=k+1, algorithm=\"brute\", metric=metric)\n",
    "    kNN.fit(X)\n",
    "    neighbour = kNN.kneighbors(movie_vec, return_distance=False)\n",
    "    for i in range(0,k):\n",
    "        n = neighbour.item(i)\n",
    "        neighbour_ids.append(movie_inv_mapper[n])\n",
    "    neighbour_ids.pop(0)\n",
    "    return neighbour_ids\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36cd3dd6",
   "metadata": {},
   "source": [
    "find_similar_movies() takes in a movieId and X matrix, and outputs a list of  movies that are similar to the movieId of interest.\n",
    "\n",
    "Let's see how it works in action. We will first create another mapper that maps movieId to title so that our results are interpretable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "d2df3389",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3114, 480, 780, 260, 356, 364, 1210, 648, 1265]"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "similar_movies = find_similar_movies(1, X, movie_mapper, movie_inv_mapper, k=10)\n",
    "similar_movies"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8227addd",
   "metadata": {},
   "source": [
    "find_similar_movies() returns a list of movieId's that are most similar to your movie of interest. Let's convert these id's to titles so that we can interpret our results. To make things easier, we will create a dictionary that maps movieId to title."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "4aec704a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Because you watched Toy Story (1995):\n",
      "Toy Story 2 (1999)\n",
      "Jurassic Park (1993)\n",
      "Independence Day (a.k.a. ID4) (1996)\n",
      "Star Wars: Episode IV - A New Hope (1977)\n",
      "Forrest Gump (1994)\n",
      "Lion King, The (1994)\n",
      "Star Wars: Episode VI - Return of the Jedi (1983)\n",
      "Mission: Impossible (1996)\n",
      "Groundhog Day (1993)\n"
     ]
    }
   ],
   "source": [
    "movie_titles = dict(zip(movies['movieId'], movies['title']))\n",
    "\n",
    "movie_id = 1\n",
    "\n",
    "similar_movies = find_similar_movies(movie_id, X, movie_mapper, movie_inv_mapper, metric='cosine', k=10)\n",
    "movie_title = movie_titles[movie_id]\n",
    "\n",
    "print(f\"Because you watched {movie_title}:\")\n",
    "for i in similar_movies:\n",
    "    print(movie_titles[i])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7160a1cb",
   "metadata": {},
   "source": [
    "Lets change the metrices and see "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "5ddec5da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Because you watched Toy Story (1995):\n",
      "Toy Story 2 (1999)\n",
      "Mission: Impossible (1996)\n",
      "Independence Day (a.k.a. ID4) (1996)\n",
      "Bug's Life, A (1998)\n",
      "Nutty Professor, The (1996)\n",
      "Willy Wonka & the Chocolate Factory (1971)\n",
      "Babe (1995)\n",
      "Groundhog Day (1993)\n",
      "Mask, The (1994)\n"
     ]
    }
   ],
   "source": [
    "movie_id = 1\n",
    "\n",
    "similar_movies = find_similar_movies(movie_id, X, movie_mapper, movie_inv_mapper, metric='euclidean', k=10)\n",
    "movie_title = movie_titles[movie_id]\n",
    "\n",
    "print(f\"Because you watched {movie_title}:\")\n",
    "for i in similar_movies:\n",
    "    print(movie_titles[i])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b3911ba",
   "metadata": {},
   "source": [
    "### Handling The Cold Start Problem\n",
    "\n",
    "The issue with Collaborative Filtering is that the new users or items with no iteractions gets excluded from the recommendation system. And as we can see since the sparsity of our utility matrix is large, we have this problem in this dataset. Content-based filtering is a way to handle this problem by generating recommendations based on users previous actions or explicit feedback by recommending other items similar to what the users like\n",
    "\n",
    "Converting 'genres' into binary digits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "ecdb55fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 9742 unique movies in our movies dataset.\n"
     ]
    }
   ],
   "source": [
    "n_movies = movies['movieId'].nunique()\n",
    "print(f\"There are {n_movies} unique movies in our movies dataset.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "0f5e8936",
   "metadata": {},
   "outputs": [],
   "source": [
    "genres = set(g for G in movies['genres'] for g in G)\n",
    "\n",
    "for g in genres:\n",
    "    movies[g] = movies.genres.transform(lambda x: int(g in x))\n",
    "\n",
    "movie_genres = movies.drop(columns=['movieId','title', 'genres'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "b7853c15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Crime</th>\n",
       "      <th>Musical</th>\n",
       "      <th>Romance</th>\n",
       "      <th>Fantasy</th>\n",
       "      <th>Documentary</th>\n",
       "      <th>Comedy</th>\n",
       "      <th>Children</th>\n",
       "      <th>Drama</th>\n",
       "      <th>Horror</th>\n",
       "      <th>(no genres listed)</th>\n",
       "      <th>Animation</th>\n",
       "      <th>Mystery</th>\n",
       "      <th>Western</th>\n",
       "      <th>Action</th>\n",
       "      <th>IMAX</th>\n",
       "      <th>Thriller</th>\n",
       "      <th>Sci-Fi</th>\n",
       "      <th>Film-Noir</th>\n",
       "      <th>Adventure</th>\n",
       "      <th>War</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Crime  Musical  Romance  Fantasy  Documentary  Comedy  Children  Drama  \\\n",
       "0      0        0        0        1            0       1         1      0   \n",
       "1      0        0        0        1            0       0         1      0   \n",
       "2      0        0        1        0            0       1         0      0   \n",
       "3      0        0        1        0            0       1         0      1   \n",
       "4      0        0        0        0            0       1         0      0   \n",
       "\n",
       "   Horror  (no genres listed)  Animation  Mystery  Western  Action  IMAX  \\\n",
       "0       0                   0          1        0        0       0     0   \n",
       "1       0                   0          0        0        0       0     0   \n",
       "2       0                   0          0        0        0       0     0   \n",
       "3       0                   0          0        0        0       0     0   \n",
       "4       0                   0          0        0        0       0     0   \n",
       "\n",
       "   Thriller  Sci-Fi  Film-Noir  Adventure  War  \n",
       "0         0       0          0          1    0  \n",
       "1         0       0          0          1    0  \n",
       "2         0       0          0          0    0  \n",
       "3         0       0          0          0    0  \n",
       "4         0       0          0          0    0  "
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_genres.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "58be39fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dimensions of our genres cosine similarity matrix: (9742, 9742)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "\n",
    "cosine_sim = cosine_similarity(movie_genres, movie_genres)\n",
    "print(f\"Dimensions of our genres cosine similarity matrix: {cosine_sim.shape}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "35096189",
   "metadata": {},
   "source": [
    "### Movie Finder\n",
    "\n",
    "To get results from our recommender, we need to know the exact title of a movie in our dataset. If we misspell the title or forget to include the year of release, our recommender wont identify which movie we are talking about. Therefore, we will use the package fuzzywuzzy to find the most similar title to the string that we input"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "9763e3f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/fuzzywuzzy/fuzz.py:11: UserWarning: Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning\n",
      "  warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')\n"
     ]
    }
   ],
   "source": [
    "from fuzzywuzzy import process\n",
    "\n",
    "def movie_finder(title):\n",
    "    all_titles = movies['title'].tolist()\n",
    "    closest_match = process.extractOne(title,all_titles)\n",
    "    return closest_match[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "edd1bcf7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Speed (1994)'"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title = movie_finder('speed')\n",
    "title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "14d2bd7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Fair Game (1995)'"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title = movie_finder('game')\n",
    "title"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "543cf54d",
   "metadata": {},
   "source": [
    "\n",
    "to get relevant recommendations, we need to find the movies index in the cosine similarity matrix for this, we can create a movie index mapper that maps a movie title to the index that it represent in the matrix therefore we use a dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "1763c579",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Movie index for Jumanji: 63\n"
     ]
    }
   ],
   "source": [
    "movie_idx = dict(zip(movies['title'], list(movies.index)))\n",
    "idx = movie_idx[title]\n",
    "print(f\"Movie index for Jumanji: {idx}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f176cb17",
   "metadata": {},
   "source": [
    "\t\n",
    "Using this handy movie_idx dictionary, we know that Jumanji is represented by index 1 in our matrix. Let's get the top 10 most similar movies to Jumanji."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "55ccfedd",
   "metadata": {},
   "outputs": [],
   "source": [
    "n_recommendations=10\n",
    "sim_scores = list(enumerate(cosine_sim[idx]))\n",
    "sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)\n",
    "sim_scores = sim_scores[1:(n_recommendations+1)]\n",
    "similar_movies = [i[0] for i in sim_scores]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c70fc30",
   "metadata": {},
   "source": [
    "similar_movies is an array of indices that represents Jumanji's top 10 recommendations. We can get the corresponding movie titles by either creating an inverse movie_idx mapper or using iloc on the title column of the movies dataframe."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "da336029",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Because you watched Fair Game (1995):\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "63                                       Fair Game (1995)\n",
       "172                  Under Siege 2: Dark Territory (1995)\n",
       "215                                    Hunted, The (1995)\n",
       "555     Bloodsport 2 (a.k.a. Bloodsport II: The Next K...\n",
       "876            Best of the Best 3: No Turning Back (1995)\n",
       "1143                                   Double Team (1997)\n",
       "1201                                         Steel (1997)\n",
       "1647                                     Knock Off (1998)\n",
       "1910                                     Avalanche (1978)\n",
       "2120                          Aces: Iron Eagle III (1992)\n",
       "Name: title, dtype: object"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(f\"Because you watched {title}:\")\n",
    "movies['title'].iloc[similar_movies]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "e2632188",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_content_based_recommendations(title_string, n_recommendations=10):\n",
    "    title = movie_finder(title_string)\n",
    "    idx = movie_idx[title]\n",
    "    sim_scores = list(enumerate(cosine_sim[idx]))\n",
    "    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)\n",
    "    sim_scores = sim_scores[1:(n_recommendations+1)]\n",
    "    similar_movies = [i[0] for i in sim_scores]\n",
    "    print(f\"Because you watched {title}:\")\n",
    "    print(movies['title'].iloc[similar_movies])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "9bc967bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Because you watched Interstellar (2014):\n",
      "6996         Monsters vs. Aliens (2009)\n",
      "7687                   Contagion (2011)\n",
      "8013                 Cloud Atlas (2012)\n",
      "8252                     Gravity (2013)\n",
      "8406    The Amazing Spider-Man 2 (2014)\n",
      "Name: title, dtype: object\n"
     ]
    }
   ],
   "source": [
    "\t\n",
    "get_content_based_recommendations('intersteller', 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38442989",
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
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
