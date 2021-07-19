def findDecision(obj): #obj[0]: age, obj[1]: job, obj[2]: marital, obj[3]: education, obj[4]: default, obj[5]: housing, obj[6]: loan, obj[7]: contact, obj[8]: month, obj[9]: day_of_week, obj[10]: duration, obj[11]: campaign, obj[12]: pdays, obj[13]: previous, obj[14]: poutcome, obj[15]: emp.var.rate, obj[16]: cons.price.idx, obj[17]: cons.conf.idx, obj[18]: euribor3m, obj[19]: nr.employed
	# {"feature": "duration", "instances": 3155, "metric_value": 0.1934, "depth": 1}
	if obj[10]<=998.4757492798608:
		# {"feature": "euribor3m", "instances": 3085, "metric_value": 0.1383, "depth": 2}
		if obj[18]<=4.857:
			# {"feature": "campaign", "instances": 1922, "metric_value": 0.0969, "depth": 3}
			if obj[11]<=6:
				# {"feature": "marital", "instances": 1870, "metric_value": 0.099, "depth": 4}
				if obj[2] == 'married':
					# {"feature": "age", "instances": 1279, "metric_value": 0.092, "depth": 5}
					if obj[0]<=59.052459212979244:
						# {"feature": "job", "instances": 1263, "metric_value": 0.093, "depth": 6}
						if obj[1] == 'blue-collar':
							# {"feature": "loan", "instances": 401, "metric_value": 0.0967, "depth": 7}
							if obj[6] == 'no':
								# {"feature": "education", "instances": 341, "metric_value": 0.0727, "depth": 8}
								if obj[3] == 'basic.9y':
									# {"feature": "default", "instances": 119, "metric_value": 0.07, "depth": 9}
									if obj[4] == 'no':
										return 'no'
									elif obj[4] == 'unknown':
										# {"feature": "housing", "instances": 43, "metric_value": 0.1594, "depth": 10}
										if obj[5] == 'no':
											return 'no'
										elif obj[5] == 'yes':
											# {"feature": "day_of_week", "instances": 21, "metric_value": 0.2762, "depth": 11}
											if obj[9] == 'tue':
												return 'no'
											elif obj[9] == 'mon':
												# {"feature": "contact", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 6, "metric_value": 0.65, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 6, "metric_value": 0.65, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 6, "metric_value": 0.65, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 6, "metric_value": 0.65, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[9] == 'fri':
												return 'no'
											elif obj[9] == 'wed':
												return 'no'
											elif obj[9] == 'thu':
												return 'no'
											else: return 'no'
										else: return 'no'
									else: return 'no'
								elif obj[3] == 'basic.4y':
									# {"feature": "day_of_week", "instances": 103, "metric_value": 0.1382, "depth": 9}
									if obj[9] == 'tue':
										# {"feature": "housing", "instances": 34, "metric_value": 0.1914, "depth": 10}
										if obj[5] == 'yes':
											return 'no'
										elif obj[5] == 'no':
											# {"feature": "default", "instances": 16, "metric_value": 0.3373, "depth": 11}
											if obj[4] == 'unknown':
												# {"feature": "contact", "instances": 11, "metric_value": 0.4395, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 11, "metric_value": 0.4395, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 11, "metric_value": 0.4395, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 11, "metric_value": 0.4395, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 11, "metric_value": 0.4395, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 11, "metric_value": 0.4395, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 11, "metric_value": 0.4395, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 11, "metric_value": 0.4395, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 11, "metric_value": 0.4395, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[4] == 'no':
												return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[9] == 'mon':
										return 'no'
									elif obj[9] == 'thu':
										return 'no'
									elif obj[9] == 'wed':
										# {"feature": "housing", "instances": 16, "metric_value": 0.3373, "depth": 10}
										if obj[5] == 'no':
											return 'no'
										elif obj[5] == 'yes':
											# {"feature": "default", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[4] == 'unknown':
												return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[9] == 'fri':
										return 'no'
									else: return 'no'
								elif obj[3] == 'basic.6y':
									return 'no'
								elif obj[3] == 'professional.course':
									return 'no'
								elif obj[3] == 'high.school':
									return 'no'
								elif obj[3] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[6] == 'yes':
								# {"feature": "housing", "instances": 52, "metric_value": 0.2352, "depth": 8}
								if obj[5] == 'no':
									return 'no'
								elif obj[5] == 'yes':
									# {"feature": "default", "instances": 25, "metric_value": 0.4022, "depth": 9}
									if obj[4] == 'no':
										# {"feature": "education", "instances": 13, "metric_value": 0.6194, "depth": 10}
										if obj[3] == 'basic.9y':
											# {"feature": "day_of_week", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[9] == 'fri':
												return 'no'
											elif obj[9] == 'mon':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[9] == 'tue':
												return 'no'
											else: return 'no'
										elif obj[3] == 'basic.6y':
											return 'no'
										elif obj[3] == 'basic.4y':
											return 'no'
										elif obj[3] == 'unknown':
											return 'no'
										elif obj[3] == 'professional.course':
											return 'yes'
										elif obj[3] == 'high.school':
											return 'no'
										else: return 'no'
									elif obj[4] == 'unknown':
										return 'no'
									else: return 'no'
								else: return 'no'
							elif obj[6] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[1] == 'admin.':
							# {"feature": "housing", "instances": 235, "metric_value": 0.0707, "depth": 7}
							if obj[5] == 'yes':
								return 'no'
							elif obj[5] == 'no':
								# {"feature": "day_of_week", "instances": 107, "metric_value": 0.134, "depth": 8}
								if obj[9] == 'tue':
									return 'no'
								elif obj[9] == 'fri':
									return 'no'
								elif obj[9] == 'mon':
									# {"feature": "education", "instances": 17, "metric_value": 0.3228, "depth": 9}
									if obj[3] == 'high.school':
										return 'no'
									elif obj[3] == 'university.degree':
										# {"feature": "loan", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[6] == 'no':
											# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[6] == 'yes':
											return 'no'
										else: return 'no'
									elif obj[3] == 'basic.9y':
										return 'no'
									elif obj[3] == 'unknown':
										return 'no'
									elif obj[3] == 'basic.6y':
										return 'no'
									elif obj[3] == 'professional.course':
										return 'no'
									else: return 'no'
								elif obj[9] == 'wed':
									return 'no'
								elif obj[9] == 'thu':
									# {"feature": "education", "instances": 10, "metric_value": 0.469, "depth": 9}
									if obj[3] == 'university.degree':
										# {"feature": "default", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[4] == 'unknown':
											return 'no'
										else: return 'no'
									elif obj[3] == 'high.school':
										return 'no'
									elif obj[3] == 'basic.6y':
										return 'no'
									else: return 'no'
								else: return 'no'
							elif obj[5] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[1] == 'technician':
							# {"feature": "default", "instances": 161, "metric_value": 0.1678, "depth": 7}
							if obj[4] == 'no':
								# {"feature": "education", "instances": 118, "metric_value": 0.2136, "depth": 8}
								if obj[3] == 'professional.course':
									# {"feature": "day_of_week", "instances": 63, "metric_value": 0.1176, "depth": 9}
									if obj[9] == 'tue':
										return 'no'
									elif obj[9] == 'fri':
										# {"feature": "housing", "instances": 15, "metric_value": 0.3534, "depth": 10}
										if obj[5] == 'no':
											# {"feature": "loan", "instances": 9, "metric_value": 0.5033, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 7, "metric_value": 0.5917, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 7, "metric_value": 0.5917, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 7, "metric_value": 0.5917, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 7, "metric_value": 0.5917, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 7, "metric_value": 0.5917, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 7, "metric_value": 0.5917, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[5] == 'yes':
											return 'no'
										else: return 'no'
									elif obj[9] == 'thu':
										return 'no'
									elif obj[9] == 'wed':
										return 'no'
									elif obj[9] == 'mon':
										return 'no'
									else: return 'no'
								elif obj[3] == 'university.degree':
									# {"feature": "housing", "instances": 24, "metric_value": 0.4138, "depth": 9}
									if obj[5] == 'yes':
										# {"feature": "day_of_week", "instances": 12, "metric_value": 0.65, "depth": 10}
										if obj[9] == 'tue':
											# {"feature": "loan", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[9] == 'fri':
											return 'no'
										elif obj[9] == 'mon':
											return 'no'
										elif obj[9] == 'thu':
											return 'no'
										else: return 'no'
									elif obj[5] == 'no':
										return 'no'
									else: return 'no'
								elif obj[3] == 'basic.9y':
									return 'no'
								elif obj[3] == 'high.school':
									# {"feature": "day_of_week", "instances": 12, "metric_value": 0.4138, "depth": 9}
									if obj[9] == 'wed':
										return 'no'
									elif obj[9] == 'fri':
										return 'no'
									elif obj[9] == 'mon':
										return 'no'
									elif obj[9] == 'tue':
										return 'no'
									elif obj[9] == 'thu':
										return 'yes'
									else: return 'yes'
								elif obj[3] == 'basic.6y':
									return 'no'
								elif obj[3] == 'basic.4y':
									return 'no'
								elif obj[3] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[4] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[1] == 'services':
							# {"feature": "default", "instances": 151, "metric_value": 0.0575, "depth": 7}
							if obj[4] == 'no':
								return 'no'
							elif obj[4] == 'unknown':
								# {"feature": "day_of_week", "instances": 49, "metric_value": 0.1437, "depth": 8}
								if obj[9] == 'tue':
									return 'no'
								elif obj[9] == 'mon':
									return 'no'
								elif obj[9] == 'fri':
									# {"feature": "education", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[3] == 'high.school':
										# {"feature": "housing", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[5] == 'no':
											# {"feature": "loan", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[5] == 'yes':
											return 'no'
										else: return 'no'
									elif obj[3] == 'unknown':
										return 'no'
									else: return 'no'
								elif obj[9] == 'wed':
									return 'no'
								elif obj[9] == 'thu':
									return 'no'
								else: return 'no'
							else: return 'no'
						elif obj[1] == 'management':
							# {"feature": "housing", "instances": 105, "metric_value": 0.1361, "depth": 7}
							if obj[5] == 'no':
								# {"feature": "education", "instances": 61, "metric_value": 0.2082, "depth": 8}
								if obj[3] == 'university.degree':
									# {"feature": "day_of_week", "instances": 35, "metric_value": 0.1872, "depth": 9}
									if obj[9] == 'mon':
										# {"feature": "default", "instances": 11, "metric_value": 0.4395, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 7, "metric_value": 0.5917, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 7, "metric_value": 0.5917, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 7, "metric_value": 0.5917, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 7, "metric_value": 0.5917, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 7, "metric_value": 0.5917, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 7, "metric_value": 0.5917, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[4] == 'unknown':
											return 'no'
										else: return 'no'
									elif obj[9] == 'tue':
										return 'no'
									elif obj[9] == 'fri':
										return 'no'
									elif obj[9] == 'thu':
										return 'no'
									elif obj[9] == 'wed':
										return 'no'
									else: return 'no'
								elif obj[3] == 'basic.6y':
									return 'no'
								elif obj[3] == 'high.school':
									return 'no'
								elif obj[3] == 'basic.9y':
									# {"feature": "default", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[4] == 'no':
										return 'no'
									elif obj[4] == 'unknown':
										return 'yes'
									else: return 'yes'
								elif obj[3] == 'basic.4y':
									return 'no'
								elif obj[3] == 'unknown':
									return 'no'
								elif obj[3] == 'professional.course':
									return 'no'
								else: return 'no'
							elif obj[5] == 'yes':
								return 'no'
							elif obj[5] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[1] == 'entrepreneur':
							return 'no'
						elif obj[1] == 'housemaid':
							return 'no'
						elif obj[1] == 'unemployed':
							return 'no'
						elif obj[1] == 'retired':
							# {"feature": "day_of_week", "instances": 32, "metric_value": 0.2006, "depth": 7}
							if obj[9] == 'tue':
								return 'no'
							elif obj[9] == 'mon':
								return 'no'
							elif obj[9] == 'thu':
								return 'no'
							elif obj[9] == 'fri':
								# {"feature": "education", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[3] == 'basic.4y':
									return 'no'
								elif obj[3] == 'high.school':
									# {"feature": "default", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4] == 'no':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'no':
											# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									else: return 'no'
								else: return 'no'
							elif obj[9] == 'wed':
								return 'no'
							else: return 'no'
						elif obj[1] == 'self-employed':
							return 'no'
						elif obj[1] == 'unknown':
							return 'no'
						else: return 'no'
					elif obj[0]>59.052459212979244:
						return 'no'
					else: return 'no'
				elif obj[2] == 'single':
					# {"feature": "age", "instances": 373, "metric_value": 0.1345, "depth": 5}
					if obj[0]<=50.624912187523634:
						# {"feature": "day_of_week", "instances": 356, "metric_value": 0.1234, "depth": 6}
						if obj[9] == 'tue':
							# {"feature": "education", "instances": 108, "metric_value": 0.0758, "depth": 7}
							if obj[3] == 'university.degree':
								return 'no'
							elif obj[3] == 'high.school':
								return 'no'
							elif obj[3] == 'basic.9y':
								# {"feature": "housing", "instances": 18, "metric_value": 0.3095, "depth": 8}
								if obj[5] == 'no':
									# {"feature": "default", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[4] == 'no':
										# {"feature": "job", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[1] == 'blue-collar':
											# {"feature": "loan", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[1] == 'management':
											return 'no'
										elif obj[1] == 'entrepreneur':
											return 'no'
										else: return 'no'
									elif obj[4] == 'unknown':
										return 'no'
									else: return 'no'
								elif obj[5] == 'yes':
									return 'no'
								elif obj[5] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[3] == 'unknown':
								return 'no'
							elif obj[3] == 'professional.course':
								return 'no'
							elif obj[3] == 'basic.6y':
								return 'no'
							elif obj[3] == 'basic.4y':
								return 'no'
							else: return 'no'
						elif obj[9] == 'fri':
							# {"feature": "housing", "instances": 81, "metric_value": 0.096, "depth": 7}
							if obj[5] == 'no':
								return 'no'
							elif obj[5] == 'yes':
								# {"feature": "education", "instances": 37, "metric_value": 0.1793, "depth": 8}
								if obj[3] == 'university.degree':
									return 'no'
								elif obj[3] == 'basic.9y':
									return 'no'
								elif obj[3] == 'high.school':
									# {"feature": "job", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[1] == 'services':
										# {"feature": "default", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[4] == 'unknown':
											return 'no'
										else: return 'no'
									elif obj[1] == 'admin.':
										return 'no'
									elif obj[1] == 'technician':
										return 'no'
									else: return 'no'
								elif obj[3] == 'professional.course':
									return 'no'
								elif obj[3] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[5] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[9] == 'mon':
							# {"feature": "job", "instances": 76, "metric_value": 0.1011, "depth": 7}
							if obj[1] == 'admin.':
								return 'no'
							elif obj[1] == 'blue-collar':
								return 'no'
							elif obj[1] == 'technician':
								return 'no'
							elif obj[1] == 'services':
								# {"feature": "housing", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[5] == 'no':
									# {"feature": "default", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[4] == 'no':
										# {"feature": "education", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3] == 'basic.9y':
											return 'no'
										elif obj[3] == 'basic.6y':
											return 'no'
										elif obj[3] == 'basic.4y':
											return 'no'
										elif obj[3] == 'high.school':
											return 'yes'
										else: return 'yes'
									elif obj[4] == 'unknown':
										return 'no'
									else: return 'no'
								elif obj[5] == 'yes':
									return 'no'
								elif obj[5] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[1] == 'student':
								return 'no'
							elif obj[1] == 'management':
								return 'no'
							elif obj[1] == 'housemaid':
								return 'no'
							elif obj[1] == 'unemployed':
								return 'no'
							elif obj[1] == 'self-employed':
								return 'no'
							elif obj[1] == 'entrepreneur':
								return 'no'
							else: return 'no'
						elif obj[9] == 'thu':
							return 'no'
						elif obj[9] == 'wed':
							# {"feature": "education", "instances": 40, "metric_value": 0.3843, "depth": 7}
							if obj[3] == 'university.degree':
								# {"feature": "housing", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[5] == 'yes':
									return 'no'
								elif obj[5] == 'no':
									# {"feature": "job", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[1] == 'admin.':
										# {"feature": "default", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									else: return 'no'
								elif obj[5] == 'unknown':
									return 'no'
								else: return 'no'
							elif obj[3] == 'high.school':
								return 'no'
							elif obj[3] == 'basic.9y':
								# {"feature": "housing", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[5] == 'no':
									return 'no'
								elif obj[5] == 'yes':
									return 'yes'
								else: return 'yes'
							elif obj[3] == 'unknown':
								return 'no'
							elif obj[3] == 'basic.4y':
								return 'no'
							elif obj[3] == 'professional.course':
								return 'no'
							elif obj[3] == 'basic.6y':
								return 'no'
							else: return 'no'
						else: return 'no'
					elif obj[0]>50.624912187523634:
						# {"feature": "education", "instances": 17, "metric_value": 0.3228, "depth": 6}
						if obj[3] == 'high.school':
							return 'no'
						elif obj[3] == 'university.degree':
							return 'no'
						elif obj[3] == 'basic.9y':
							return 'no'
						elif obj[3] == 'professional.course':
							return 'no'
						elif obj[3] == 'basic.6y':
							return 'yes'
						elif obj[3] == 'basic.4y':
							return 'no'
						else: return 'no'
					else: return 'no'
				elif obj[2] == 'divorced':
					# {"feature": "age", "instances": 215, "metric_value": 0.0427, "depth": 5}
					if obj[0]<=52.69115832390763:
						return 'no'
					elif obj[0]>52.69115832390763:
						# {"feature": "day_of_week", "instances": 49, "metric_value": 0.1437, "depth": 6}
						if obj[9] == 'tue':
							return 'no'
						elif obj[9] == 'fri':
							# {"feature": "default", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[4] == 'no':
								# {"feature": "education", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[3] == 'university.degree':
									# {"feature": "job", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1] == 'admin.':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[1] == 'technician':
										return 'no'
									else: return 'no'
								elif obj[3] == 'high.school':
									return 'no'
								elif obj[3] == 'professional.course':
									return 'no'
								else: return 'no'
							elif obj[4] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[9] == 'mon':
							return 'no'
						elif obj[9] == 'wed':
							return 'no'
						elif obj[9] == 'thu':
							return 'no'
						else: return 'no'
					else: return 'no'
				elif obj[2] == 'unknown':
					# {"feature": "job", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == 'unknown':
						return 'yes'
					elif obj[1] == 'blue-collar':
						return 'no'
					elif obj[1] == 'management':
						return 'no'
					else: return 'no'
				else: return 'no'
			elif obj[11]>6:
				return 'no'
			else: return 'no'
		elif obj[18]>4.857:
			# {"feature": "age", "instances": 1163, "metric_value": 0.1992, "depth": 3}
			if obj[0]>22:
				# {"feature": "job", "instances": 1162, "metric_value": 0.1993, "depth": 4}
				if obj[1] == 'blue-collar':
					# {"feature": "campaign", "instances": 377, "metric_value": 0.1627, "depth": 5}
					if obj[11]<=17:
						# {"feature": "education", "instances": 376, "metric_value": 0.1485, "depth": 6}
						if obj[3] == 'basic.9y':
							# {"feature": "housing", "instances": 160, "metric_value": 0.1344, "depth": 7}
							if obj[5] == 'no':
								# {"feature": "marital", "instances": 85, "metric_value": 0.2203, "depth": 8}
								if obj[2] == 'married':
									# {"feature": "loan", "instances": 62, "metric_value": 0.2795, "depth": 9}
									if obj[6] == 'no':
										# {"feature": "day_of_week", "instances": 54, "metric_value": 0.3095, "depth": 10}
										if obj[9] == 'wed':
											# {"feature": "default", "instances": 23, "metric_value": 0.4262, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 15, "metric_value": 0.3534, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 15, "metric_value": 0.3534, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 15, "metric_value": 0.3534, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 15, "metric_value": 0.3534, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 15, "metric_value": 0.3534, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 15, "metric_value": 0.3534, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 15, "metric_value": 0.3534, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 15, "metric_value": 0.3534, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 15, "metric_value": 0.3534, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[4] == 'unknown':
												# {"feature": "contact", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 8, "metric_value": 0.5436, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 8, "metric_value": 0.5436, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 8, "metric_value": 0.5436, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 8, "metric_value": 0.5436, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 8, "metric_value": 0.5436, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 8, "metric_value": 0.5436, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[9] == 'thu':
											# {"feature": "default", "instances": 13, "metric_value": 0.3912, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 9, "metric_value": 0.5033, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 9, "metric_value": 0.5033, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 9, "metric_value": 0.5033, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 9, "metric_value": 0.5033, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 9, "metric_value": 0.5033, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 9, "metric_value": 0.5033, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[4] == 'unknown':
												return 'no'
											else: return 'no'
										elif obj[9] == 'fri':
											return 'no'
										elif obj[9] == 'mon':
											return 'no'
										else: return 'no'
									elif obj[6] == 'yes':
										return 'no'
									else: return 'no'
								elif obj[2] == 'single':
									return 'no'
								elif obj[2] == 'divorced':
									return 'no'
								else: return 'no'
							elif obj[5] == 'yes':
								return 'no'
							elif obj[5] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[3] == 'basic.4y':
							return 'no'
						elif obj[3] == 'basic.6y':
							# {"feature": "day_of_week", "instances": 65, "metric_value": 0.2698, "depth": 7}
							if obj[9] == 'wed':
								# {"feature": "marital", "instances": 27, "metric_value": 0.5033, "depth": 8}
								if obj[2] == 'married':
									# {"feature": "housing", "instances": 23, "metric_value": 0.5586, "depth": 9}
									if obj[5] == 'no':
										# {"feature": "loan", "instances": 13, "metric_value": 0.3912, "depth": 10}
										if obj[6] == 'no':
											return 'no'
										elif obj[6] == 'yes':
											# {"feature": "default", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[5] == 'yes':
										# {"feature": "loan", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[6] == 'no':
											# {"feature": "default", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[4] == 'no':
												# {"feature": "contact", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[4] == 'unknown':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[6] == 'yes':
											return 'no'
										else: return 'no'
									elif obj[5] == 'unknown':
										return 'no'
									else: return 'no'
								elif obj[2] == 'single':
									return 'no'
								elif obj[2] == 'divorced':
									return 'no'
								else: return 'no'
							elif obj[9] == 'mon':
								return 'no'
							elif obj[9] == 'fri':
								return 'no'
							elif obj[9] == 'thu':
								return 'no'
							else: return 'no'
						elif obj[3] == 'high.school':
							# {"feature": "default", "instances": 25, "metric_value": 0.4022, "depth": 7}
							if obj[4] == 'no':
								# {"feature": "loan", "instances": 20, "metric_value": 0.469, "depth": 8}
								if obj[6] == 'no':
									# {"feature": "day_of_week", "instances": 16, "metric_value": 0.5436, "depth": 9}
									if obj[9] == 'wed':
										# {"feature": "marital", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[2] == 'married':
											# {"feature": "housing", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[5] == 'no':
												# {"feature": "contact", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[5] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[2] == 'single':
											return 'no'
										elif obj[2] == 'divorced':
											return 'no'
										else: return 'no'
									elif obj[9] == 'fri':
										# {"feature": "marital", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2] == 'married':
											return 'no'
										elif obj[2] == 'single':
											return 'yes'
										else: return 'yes'
									elif obj[9] == 'thu':
										return 'no'
									elif obj[9] == 'mon':
										return 'no'
									else: return 'no'
								elif obj[6] == 'yes':
									return 'no'
								else: return 'no'
							elif obj[4] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[3] == 'unknown':
							return 'no'
						elif obj[3] == 'professional.course':
							return 'no'
						elif obj[3] == 'university.degree':
							return 'no'
						else: return 'no'
					elif obj[11]>17:
						return 'yes'
					else: return 'yes'
				elif obj[1] == 'admin.':
					# {"feature": "education", "instances": 236, "metric_value": 0.2531, "depth": 5}
					if obj[3] == 'university.degree':
						# {"feature": "campaign", "instances": 107, "metric_value": 0.134, "depth": 6}
						if obj[11]<=2:
							# {"feature": "day_of_week", "instances": 66, "metric_value": 0.1959, "depth": 7}
							if obj[9] == 'wed':
								# {"feature": "housing", "instances": 26, "metric_value": 0.2352, "depth": 8}
								if obj[5] == 'yes':
									return 'no'
								elif obj[5] == 'no':
									# {"feature": "marital", "instances": 10, "metric_value": 0.469, "depth": 9}
									if obj[2] == 'single':
										# {"feature": "default", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 6, "metric_value": 0.65, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 6, "metric_value": 0.65, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 6, "metric_value": 0.65, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 6, "metric_value": 0.65, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[2] == 'married':
										return 'no'
									elif obj[2] == 'divorced':
										return 'no'
									else: return 'no'
								else: return 'no'
							elif obj[9] == 'fri':
								return 'no'
							elif obj[9] == 'thu':
								# {"feature": "housing", "instances": 13, "metric_value": 0.3912, "depth": 8}
								if obj[5] == 'yes':
									# {"feature": "marital", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[2] == 'married':
										# {"feature": "default", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[4] == 'no':
											# {"feature": "loan", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										elif obj[4] == 'unknown':
											return 'no'
										else: return 'no'
									elif obj[2] == 'divorced':
										return 'no'
									elif obj[2] == 'single':
										return 'no'
									else: return 'no'
								elif obj[5] == 'no':
									return 'no'
								else: return 'no'
							elif obj[9] == 'mon':
								return 'no'
							else: return 'no'
						elif obj[11]>2:
							return 'no'
						else: return 'no'
					elif obj[3] == 'high.school':
						# {"feature": "default", "instances": 88, "metric_value": 0.3147, "depth": 6}
						if obj[4] == 'no':
							# {"feature": "campaign", "instances": 75, "metric_value": 0.3534, "depth": 7}
							if obj[11]<=4:
								# {"feature": "marital", "instances": 66, "metric_value": 0.3871, "depth": 8}
								if obj[2] == 'married':
									# {"feature": "day_of_week", "instances": 36, "metric_value": 0.1831, "depth": 9}
									if obj[9] == 'wed':
										return 'no'
									elif obj[9] == 'fri':
										return 'no'
									elif obj[9] == 'thu':
										# {"feature": "housing", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "loan", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[6] == 'yes':
												return 'no'
											else: return 'no'
										elif obj[5] == 'no':
											return 'no'
										elif obj[5] == 'unknown':
											return 'no'
										else: return 'no'
									elif obj[9] == 'mon':
										return 'no'
									else: return 'no'
								elif obj[2] == 'single':
									# {"feature": "housing", "instances": 21, "metric_value": 0.5917, "depth": 9}
									if obj[5] == 'no':
										# {"feature": "loan", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[6] == 'no':
											# {"feature": "day_of_week", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[9] == 'wed':
												# {"feature": "contact", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 6, "metric_value": 0.65, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 6, "metric_value": 0.65, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 6, "metric_value": 0.65, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 6, "metric_value": 0.65, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[9] == 'fri':
												return 'no'
											else: return 'no'
										elif obj[6] == 'yes':
											# {"feature": "day_of_week", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[9] == 'thu':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											elif obj[9] == 'mon':
												return 'no'
											elif obj[9] == 'fri':
												return 'yes'
											else: return 'yes'
										else: return 'no'
									elif obj[5] == 'yes':
										return 'no'
									elif obj[5] == 'unknown':
										return 'no'
									else: return 'no'
								elif obj[2] == 'divorced':
									# {"feature": "day_of_week", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[9] == 'wed':
										return 'no'
									elif obj[9] == 'thu':
										return 'no'
									elif obj[9] == 'mon':
										return 'no'
									elif obj[9] == 'fri':
										return 'yes'
									else: return 'yes'
								else: return 'no'
							elif obj[11]>4:
								return 'no'
							else: return 'no'
						elif obj[4] == 'unknown':
							return 'no'
						else: return 'no'
					elif obj[3] == 'basic.9y':
						return 'no'
					elif obj[3] == 'professional.course':
						# {"feature": "loan", "instances": 14, "metric_value": 0.5917, "depth": 6}
						if obj[6] == 'no':
							# {"feature": "marital", "instances": 13, "metric_value": 0.3912, "depth": 7}
							if obj[2] == 'married':
								return 'no'
							elif obj[2] == 'divorced':
								return 'no'
							elif obj[2] == 'single':
								# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5] == 'no':
									return 'no'
								elif obj[5] == 'yes':
									return 'yes'
								else: return 'yes'
							else: return 'no'
						elif obj[6] == 'yes':
							return 'yes'
						else: return 'yes'
					elif obj[3] == 'unknown':
						return 'no'
					elif obj[3] == 'basic.4y':
						# {"feature": "default", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4] == 'no':
							return 'no'
						elif obj[4] == 'unknown':
							return 'yes'
						else: return 'yes'
					elif obj[3] == 'basic.6y':
						return 'no'
					else: return 'no'
				elif obj[1] == 'technician':
					# {"feature": "campaign", "instances": 144, "metric_value": 0.2175, "depth": 5}
					if obj[11]<=2:
						# {"feature": "default", "instances": 100, "metric_value": 0.2864, "depth": 6}
						if obj[4] == 'no':
							# {"feature": "education", "instances": 77, "metric_value": 0.1738, "depth": 7}
							if obj[3] == 'professional.course':
								return 'no'
							elif obj[3] == 'university.degree':
								# {"feature": "marital", "instances": 19, "metric_value": 0.2975, "depth": 8}
								if obj[2] == 'married':
									return 'no'
								elif obj[2] == 'single':
									# {"feature": "housing", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[5] == 'no':
										return 'no'
									elif obj[5] == 'yes':
										# {"feature": "day_of_week", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[9] == 'mon':
											return 'no'
										elif obj[9] == 'wed':
											return 'yes'
										elif obj[9] == 'fri':
											return 'no'
										else: return 'no'
									elif obj[5] == 'unknown':
										return 'no'
									else: return 'no'
								else: return 'no'
							elif obj[3] == 'basic.9y':
								return 'no'
							elif obj[3] == 'high.school':
								# {"feature": "day_of_week", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[9] == 'wed':
									# {"feature": "housing", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5] == 'yes':
										# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == 'yes':
											return 'no'
										elif obj[6] == 'no':
											return 'yes'
										else: return 'yes'
									elif obj[5] == 'no':
										return 'no'
									else: return 'no'
								elif obj[9] == 'fri':
									return 'no'
								elif obj[9] == 'mon':
									return 'no'
								else: return 'no'
							elif obj[3] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[4] == 'unknown':
							# {"feature": "education", "instances": 23, "metric_value": 0.5586, "depth": 7}
							if obj[3] == 'professional.course':
								# {"feature": "day_of_week", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[9] == 'wed':
									return 'no'
								elif obj[9] == 'thu':
									# {"feature": "marital", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2] == 'married':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'no':
											return 'no'
										elif obj[5] == 'yes':
											return 'yes'
										else: return 'yes'
									elif obj[2] == 'single':
										return 'no'
									else: return 'no'
								elif obj[9] == 'fri':
									return 'no'
								elif obj[9] == 'mon':
									return 'no'
								else: return 'no'
							elif obj[3] == 'university.degree':
								# {"feature": "marital", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[2] == 'married':
									return 'no'
								elif obj[2] == 'single':
									# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == 'yes':
										return 'no'
									elif obj[5] == 'no':
										return 'yes'
									else: return 'yes'
								elif obj[2] == 'divorced':
									return 'no'
								else: return 'no'
							elif obj[3] == 'high.school':
								return 'no'
							elif obj[3] == 'basic.9y':
								return 'yes'
							elif obj[3] == 'unknown':
								return 'no'
							else: return 'no'
						else: return 'no'
					elif obj[11]>2:
						return 'no'
					else: return 'no'
				elif obj[1] == 'services':
					# {"feature": "day_of_week", "instances": 129, "metric_value": 0.1994, "depth": 5}
					if obj[9] == 'wed':
						return 'no'
					elif obj[9] == 'mon':
						# {"feature": "campaign", "instances": 26, "metric_value": 0.5159, "depth": 6}
						if obj[11]<=2:
							return 'no'
						elif obj[11]>2:
							# {"feature": "education", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[3] == 'high.school':
								# {"feature": "marital", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[2] == 'married':
									# {"feature": "default", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[4] == 'no':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									elif obj[4] == 'unknown':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'yes':
											# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'no':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									else: return 'no'
								elif obj[2] == 'divorced':
									return 'yes'
								elif obj[2] == 'single':
									return 'no'
								else: return 'no'
							elif obj[3] == 'professional.course':
								return 'no'
							elif obj[3] == 'basic.9y':
								return 'no'
							elif obj[3] == 'university.degree':
								return 'no'
							elif obj[3] == 'unknown':
								return 'no'
							else: return 'no'
						else: return 'no'
					elif obj[9] == 'fri':
						return 'no'
					elif obj[9] == 'thu':
						# {"feature": "education", "instances": 22, "metric_value": 0.2668, "depth": 6}
						if obj[3] == 'high.school':
							return 'no'
						elif obj[3] == 'basic.9y':
							# {"feature": "housing", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5] == 'yes':
								return 'no'
							elif obj[5] == 'no':
								return 'yes'
							else: return 'yes'
						elif obj[3] == 'professional.course':
							return 'no'
						elif obj[3] == 'basic.4y':
							return 'no'
						else: return 'no'
					else: return 'no'
				elif obj[1] == 'management':
					return 'no'
				elif obj[1] == 'entrepreneur':
					# {"feature": "loan", "instances": 43, "metric_value": 0.2714, "depth": 5}
					if obj[6] == 'no':
						# {"feature": "day_of_week", "instances": 38, "metric_value": 0.1756, "depth": 6}
						if obj[9] == 'wed':
							return 'no'
						elif obj[9] == 'fri':
							# {"feature": "campaign", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[11]>1:
								return 'no'
							elif obj[11]<=1:
								# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3] == 'basic.4y':
									return 'no'
								elif obj[3] == 'university.degree':
									return 'yes'
								elif obj[3] == 'high.school':
									return 'no'
								else: return 'no'
							else: return 'no'
						elif obj[9] == 'thu':
							return 'no'
						elif obj[9] == 'mon':
							return 'no'
						else: return 'no'
					elif obj[6] == 'yes':
						# {"feature": "housing", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5] == 'no':
							return 'no'
						elif obj[5] == 'yes':
							return 'yes'
						else: return 'yes'
					elif obj[6] == 'unknown':
						return 'no'
					else: return 'no'
				elif obj[1] == 'housemaid':
					# {"feature": "education", "instances": 36, "metric_value": 0.4138, "depth": 5}
					if obj[3] == 'basic.4y':
						# {"feature": "marital", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[2] == 'married':
							# {"feature": "day_of_week", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[9] == 'wed':
								# {"feature": "campaign", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[11]<=1:
									# {"feature": "default", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[4] == 'no':
										return 'no'
									elif obj[4] == 'unknown':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'no':
											# {"feature": "loan", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == 'yes':
												# {"feature": "contact", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == 'telephone':
													# {"feature": "month", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == 'may':
														# {"feature": "pdays", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=999:
															# {"feature": "previous", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "poutcome", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == 'nonexistent':
																	# {"feature": "emp.var.rate", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.1:
																		# {"feature": "cons.price.idx", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=93.994:
																			# {"feature": "cons.conf.idx", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=-36.4:
																				# {"feature": "nr.employed", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=5191:
																					return 'no'
																				else: return 'no'
																			else: return 'no'
																		else: return 'no'
																	else: return 'no'
																else: return 'no'
															else: return 'no'
														else: return 'no'
													else: return 'no'
												else: return 'no'
											else: return 'no'
										else: return 'no'
									else: return 'no'
								elif obj[11]>1:
									return 'yes'
								else: return 'yes'
							elif obj[9] == 'thu':
								# {"feature": "campaign", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=2:
									return 'no'
								elif obj[11]>2:
									return 'yes'
								else: return 'yes'
							elif obj[9] == 'mon':
								return 'no'
							else: return 'no'
						elif obj[2] == 'single':
							return 'no'
						elif obj[2] == 'divorced':
							return 'no'
						else: return 'no'
					elif obj[3] == 'high.school':
						return 'no'
					elif obj[3] == 'university.degree':
						return 'no'
					elif obj[3] == 'basic.9y':
						return 'no'
					elif obj[3] == 'basic.6y':
						return 'no'
					elif obj[3] == 'unknown':
						return 'no'
					else: return 'no'
				elif obj[1] == 'self-employed':
					# {"feature": "campaign", "instances": 35, "metric_value": 0.1872, "depth": 5}
					if obj[11]>1:
						return 'no'
					elif obj[11]<=1:
						# {"feature": "education", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[3] == 'university.degree':
							return 'no'
						elif obj[3] == 'basic.4y':
							return 'no'
						elif obj[3] == 'high.school':
							return 'no'
						elif obj[3] == 'basic.9y':
							return 'no'
						elif obj[3] == 'basic.6y':
							return 'yes'
						elif obj[3] == 'professional.course':
							return 'no'
						else: return 'no'
					else: return 'no'
				elif obj[1] == 'retired':
					# {"feature": "campaign", "instances": 30, "metric_value": 0.2108, "depth": 5}
					if obj[11]>1:
						return 'no'
					elif obj[11]<=1:
						# {"feature": "education", "instances": 12, "metric_value": 0.4138, "depth": 6}
						if obj[3] == 'basic.4y':
							return 'no'
						elif obj[3] == 'basic.9y':
							return 'no'
						elif obj[3] == 'high.school':
							return 'no'
						elif obj[3] == 'professional.course':
							# {"feature": "default", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4] == 'no':
								return 'no'
							elif obj[4] == 'unknown':
								return 'yes'
							else: return 'yes'
						else: return 'no'
					else: return 'no'
				elif obj[1] == 'unemployed':
					return 'no'
				elif obj[1] == 'unknown':
					return 'no'
				elif obj[1] == 'student':
					# {"feature": "marital", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[2] == 'single':
						return 'no'
					elif obj[2] == 'married':
						return 'yes'
					else: return 'yes'
				else: return 'no'
			elif obj[0]<=22:
				return 'no'
			else: return 'no'
		else: return 'no'
	elif obj[10]>998.4757492798608:
		# {"feature": "age", "instances": 70, "metric_value": 0.9994, "depth": 2}
		if obj[0]<=55.49595398094611:
			# {"feature": "campaign", "instances": 68, "metric_value": 0.9975, "depth": 3}
			if obj[11]<=6:
				# {"feature": "job", "instances": 66, "metric_value": 0.9993, "depth": 4}
				if obj[1] == 'blue-collar':
					# {"feature": "euribor3m", "instances": 21, "metric_value": 0.9852, "depth": 5}
					if obj[18]>4.855:
						# {"feature": "education", "instances": 20, "metric_value": 0.9928, "depth": 6}
						if obj[3] == 'basic.4y':
							# {"feature": "day_of_week", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[9] == 'wed':
								# {"feature": "marital", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[2] == 'married':
									# {"feature": "default", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4] == 'unknown':
										# {"feature": "housing", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == 'no':
											return 'no'
										elif obj[5] == 'yes':
											return 'yes'
										else: return 'yes'
									elif obj[4] == 'no':
										return 'no'
									else: return 'no'
								elif obj[2] == 'single':
									return 'yes'
								else: return 'yes'
							elif obj[9] == 'fri':
								return 'no'
							elif obj[9] == 'tue':
								return 'no'
							else: return 'no'
						elif obj[3] == 'basic.9y':
							# {"feature": "default", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[4] == 'unknown':
								# {"feature": "marital", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2] == 'divorced':
									# {"feature": "day_of_week", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[9] == 'fri':
										return 'no'
									elif obj[9] == 'thu':
										return 'yes'
									else: return 'yes'
								elif obj[2] == 'single':
									return 'yes'
								else: return 'yes'
							elif obj[4] == 'no':
								return 'no'
							else: return 'no'
						elif obj[3] == 'basic.6y':
							# {"feature": "housing", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5] == 'unknown':
								return 'yes'
							elif obj[5] == 'no':
								return 'no'
							elif obj[5] == 'yes':
								return 'no'
							else: return 'no'
						elif obj[3] == 'high.school':
							return 'yes'
						elif obj[3] == 'unknown':
							return 'yes'
						else: return 'yes'
					elif obj[18]<=4.855:
						return 'no'
					else: return 'no'
				elif obj[1] == 'technician':
					# {"feature": "euribor3m", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[18]>4.855:
						# {"feature": "education", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[3] == 'university.degree':
							# {"feature": "housing", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5] == 'no':
								# {"feature": "day_of_week", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[9] == 'fri':
									return 'no'
								elif obj[9] == 'tue':
									return 'yes'
								elif obj[9] == 'mon':
									return 'no'
								else: return 'no'
							elif obj[5] == 'yes':
								return 'yes'
							else: return 'yes'
						elif obj[3] == 'professional.course':
							# {"feature": "default", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[4] == 'no':
								# {"feature": "day_of_week", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[9] == 'tue':
									return 'no'
								elif obj[9] == 'mon':
									return 'yes'
								elif obj[9] == 'wed':
									return 'yes'
								else: return 'yes'
							elif obj[4] == 'unknown':
								return 'no'
							else: return 'no'
						elif obj[3] == 'basic.9y':
							# {"feature": "housing", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5] == 'no':
								# {"feature": "day_of_week", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[9] == 'fri':
									return 'no'
								elif obj[9] == 'mon':
									return 'yes'
								else: return 'yes'
							elif obj[5] == 'yes':
								return 'no'
							else: return 'no'
						elif obj[3] == 'unknown':
							return 'yes'
						elif obj[3] == 'high.school':
							return 'no'
						else: return 'no'
					elif obj[18]<=4.855:
						return 'yes'
					else: return 'yes'
				elif obj[1] == 'services':
					# {"feature": "euribor3m", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[18]>4.855:
						# {"feature": "default", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[4] == 'no':
							return 'yes'
						elif obj[4] == 'unknown':
							# {"feature": "housing", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5] == 'no':
								# {"feature": "marital", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2] == 'single':
									return 'yes'
								elif obj[2] == 'divorced':
									return 'no'
								elif obj[2] == 'married':
									return 'yes'
								else: return 'yes'
							elif obj[5] == 'yes':
								return 'no'
							else: return 'no'
						else: return 'no'
					elif obj[18]<=4.855:
						return 'no'
					else: return 'no'
				elif obj[1] == 'admin.':
					# {"feature": "default", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[4] == 'no':
						# {"feature": "housing", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[5] == 'yes':
							return 'no'
						elif obj[5] == 'no':
							# {"feature": "education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3] == 'university.degree':
								return 'yes'
							elif obj[3] == 'basic.6y':
								return 'no'
							else: return 'no'
						else: return 'yes'
					elif obj[4] == 'unknown':
						return 'yes'
					else: return 'yes'
				elif obj[1] == 'management':
					return 'yes'
				elif obj[1] == 'unknown':
					# {"feature": "education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3] == 'unknown':
						return 'yes'
					elif obj[3] == 'basic.6y':
						return 'no'
					else: return 'no'
				elif obj[1] == 'entrepreneur':
					# {"feature": "marital", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'divorced':
						return 'no'
					elif obj[2] == 'married':
						return 'yes'
					else: return 'yes'
				elif obj[1] == 'self-employed':
					return 'no'
				elif obj[1] == 'unemployed':
					return 'no'
				else: return 'no'
			elif obj[11]>6:
				return 'no'
			else: return 'no'
		elif obj[0]>55.49595398094611:
			return 'yes'
		else: return 'yes'
	else: return 'no'
