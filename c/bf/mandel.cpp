#include<cstdio>
char m[1<<15];
int main(){
	char *p=m;
	(*p)+=13;
	while(*p){
		(*p)--;
		(*(p+1))+=2;
		(*(p+4))+=5;
		(*(p+5))+=2;
		(*(p+6))++;
	}
	(*(p+5))+=6;
	(*(p+6))-=3;
	p+=16;
	(*p)+=15;
	while(*p){
		while(*p){
			p+=9;
		}
		(*p)++;
		while(*p){
			p-=9;
		}
		p+=9;
		(*p)--;
	}
	(*p)++;
	while(*p){
		p+=8;
		(*p)=0;
		p++;
	}
	p-=9;
	while(*p){
		p-=9;
	}
	(*(p+8))=1;
	p++;
	(*p)+=5;
	while(*p){
		(*p)--;
		while(*p){
			(*p)--;
			(*(p+9))++;
		}
		p+=9;
	}
	(*(p+7))++;
	(*(p+34))++;
	p+=17;
	while(*p){
		p-=9;
	}
	p+=3;
	(*p)=1;
	while(*p){
		p+=6;
		while(*p){
			p+=7;
			(*p)=0;
			p+=2;
		}
		p-=9;
		while(*p){
			p-=9;
		}
		(*(p+7))=1;
		p++;
		(*p)+=4;
		while(*p){
			(*p)--;
			while(*p){
				(*p)--;
				(*(p+9))++;
			}
			p+=9;
		}
		(*(p+6))++;
		(*p)+=7;
		while(*p){
			(*p)--;
			while(*p){
				(*p)--;
				(*(p+9))++;
			}
			p+=9;
		}
		(*(p+6))++;
		p-=10;
		while(*p){
			p-=9;
		}
		p+=3;
		while(*p){
			(*p)=0;
			p+=6;
			while(*p){
				p+=7;
				while(*p){
					(*p)--;
					(*(p-6))++;
				}
				p-=6;
				while(*p){
					(*p)--;
					(*(p+6))++;
					(*(p+4))++;
					(*(p+1))++;
				}
				p+=8;
			}
			p-=9;
			while(*p){
				p-=9;
			}
			p+=9;
			while(*p){
				p+=8;
				while(*p){
					(*p)--;
					(*(p-7))++;
				}
				p-=7;
				while(*p){
					(*p)--;
					(*(p+7))++;
					(*(p+5))++;
					(*(p+2))++;
				}
				p+=8;
			}
			p-=9;
			while(*p){
				p-=9;
			}
			p+=7;
			while(*p){
				(*p)--;
				(*(p-7))++;
			}
			p-=7;
			while(*p){
				(*p)--;
				(*(p+7))++;
				(*(p+5))++;
			}
			p+=9;
			(*p)+=15;
			while(*p){
				while(*p){
					p+=9;
				}
				(*p)++;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				(*p)--;
			}
			(*p)++;
			while(*p){
				(*(p+1))++;
				p+=9;
			}
			p-=9;
			while(*p){
				p-=9;
			}
			p+=9;
			while(*p){
				(*(p+1))--;
				p+=5;
				while(*p){
					(*p)--;
					(*(p-4))++;
				}
				p-=4;
				while(*p){
					(*p)--;
					(*(p+4))++;
					p--;
					while(*p){
						(*p)--;
						p+=2;
						while(*p){
							(*p)--;
							(*(p-2))++;
						}
						p-=2;
						while(*p){
							(*p)--;
							(*(p+2))++;
							(*(p+4))++;
						}
						(*p)++;
						p+=9;
					}
					p-=8;
					while(*p){
						p-=9;
					}
				}
				p+=9;
				while(*p){
					p+=9;
				}
				p-=9;
				while(*p){
					p++;
					while(*p){
						(*p)--;
						(*(p+9))++;
					}
					p-=10;
				}
				p++;
				while(*p){
					(*p)--;
					(*(p+9))++;
				}
				(*(p-1))++;
				p+=7;
			}
			p-=9;
			while(*p){
				p++;
				(*p)=0;
				(*(p-1))--;
				p+=3;
				while(*p){
					(*p)--;
					(*(p-4))++;
					p-=3;
					while(*p){
						(*(p-1))--;
						(*p)--;
						(*(p-6))++;
					}
					p--;
					while(*p){
						(*p)--;
						(*(p+1))++;
					}
					p+=4;
				}
				p-=3;
				while(*p){
					(*p)--;
					(*(p+3))++;
				}
				(*(p-1))++;
				p-=10;
			}
			p+=9;
			while(*p){
				(*(p+1))++;
				p+=9;
			}
			p-=9;
			while(*p){
				p-=9;
			}
			p+=9;
			while(*p){
				(*(p+1))--;
				p+=6;
				while(*p){
					(*p)--;
					(*(p-5))++;
				}
				p-=5;
				while(*p){
					(*p)--;
					(*(p+5))++;
					p--;
					while(*p){
						(*p)--;
						p+=3;
						while(*p){
							(*p)--;
							(*(p-3))++;
						}
						p-=3;
						while(*p){
							(*p)--;
							(*(p+3))++;
							(*(p+4))++;
						}
						(*p)++;
						p+=9;
					}
					p-=8;
					while(*p){
						p-=9;
					}
				}
				p+=9;
				while(*p){
					p+=9;
				}
				p-=9;
				while(*p){
					p+=2;
					while(*p){
						(*p)--;
						(*(p+9))++;
					}
					p-=11;
				}
				p+=2;
				while(*p){
					(*p)--;
					(*(p+9))++;
				}
				(*(p-2))++;
				p+=6;
			}
			p-=9;
			while(*p){
				p++;
				(*p)=0;
				(*(p-1))--;
				p+=3;
				while(*p){
					(*p)--;
					(*(p-4))++;
					p-=3;
					while(*p){
						(*(p-1))--;
						(*p)--;
						(*(p-6))++;
					}
					p--;
					while(*p){
						(*p)--;
						(*(p+1))++;
					}
					p+=4;
				}
				p-=3;
				while(*p){
					(*p)--;
					(*(p+3))++;
				}
				(*(p-1))++;
				p-=10;
			}
			p+=9;
			while(*p){
				p+=4;
				while(*p){
					(*p)--;
					(*(p-36))++;
				}
				p+=5;
			}
			p-=9;
			while(*p){
				p-=9;
			}
			p+=9;
			(*p)+=15;
			while(*p){
				while(*p){
					p+=9;
				}
				(*(p-9))--;
				p-=18;
				while(*p){
					p-=9;
				}
				p+=9;
				(*p)--;
			}
			(*p)++;
			(*(p+21))++;
			p+=18;
			while(*p){
				p-=9;
			}
			p+=9;
			while(*p){
				p+=3;
				while(*p){
					(*p)--;
					(*(p-3))--;
				}
				(*p)++;
				p-=3;
				while(*p){
					(*p)--;
					(*(p+3))--;
					p+=4;
					while(*p){
						(*p)--;
						(*(p-4))++;
					}
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))++;
						p-=9;
						while(*p){
							p-=9;
						}
						(*(p+4))=1;
						p+=9;
						while(*p){
							p+=9;
						}
						(*(p+1))++;
					}
				}
				(*p)++;
				p+=4;
				while(*p){
					(*p)--;
					(*(p-4))--;
				}
				(*p)++;
				p-=4;
				while(*p){
					(*p)--;
					(*(p+4))--;
					p+=3;
					while(*p){
						(*p)--;
						(*(p-3))++;
					}
					p-=3;
					while(*p){
						(*p)--;
						(*(p+3))++;
						p-=9;
						while(*p){
							p-=9;
						}
						(*(p+3))=1;
						p+=9;
						while(*p){
							p+=9;
						}
						(*(p+1))=1;
					}
				}
				(*p)++;
				p++;
				while(*p){
					(*p)--;
					p--;
					while(*p){
						p+=9;
					}
					p-=8;
				}
				p+=8;
			}
			p-=9;
			while(*p){
				p-=9;
			}
			p-=7;
			while(*p){
				(*p)--;
				(*(p+1))++;
				(*(p+4))--;
			}
			(*(p+9))+=26;
			p+=11;
			while(*p){
				(*p)--;
				(*(p-4))++;
			}
			p-=4;
			while(*p){
				(*p)--;
				(*(p+4))++;
				p+=2;
				(*p)=0;
				p-=2;
			}
			p+=2;
			while(*p){
				(*(p-7))++;
				p-=8;
				while(*p){
					(*p)--;
					(*(p-1))++;
					(*(p+3))++;
					p++;
					(*p)=0;
				}
				p++;
				while(*p){
					(*p)--;
					p-=2;
					while(*p){
						(*p)--;
						(*(p+1))++;
						(*(p+4))--;
					}
					p+=3;
				}
				p+=13;
				while(*p){
					p+=2;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p+=5;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=3;
				(*p)=0;
				p+=6;
				while(*p){
					p+=5;
					while(*p){
						(*p)--;
						(*(p-4))++;
					}
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))++;
						(*(p+1))++;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					p+=2;
					while(*p){
						(*p)--;
						(*(p-9))++;
					}
					p+=7;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				(*p)+=15;
				while(*p){
					while(*p){
						p+=9;
					}
					(*p)++;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p-=9;
					while(*p){
						p-=9;
					}
					p+=9;
					(*p)--;
				}
				(*p)++;
				while(*p){
					(*(p+1))++;
					p+=9;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					(*(p+1))--;
					p+=6;
					while(*p){
						(*p)--;
						(*(p-5))++;
					}
					p-=5;
					while(*p){
						(*p)--;
						(*(p+5))++;
						p--;
						while(*p){
							(*p)--;
							p+=2;
							while(*p){
								(*p)--;
								(*(p-2))++;
							}
							p-=2;
							while(*p){
								(*p)--;
								(*(p+2))++;
								(*(p+3))++;
							}
							(*p)++;
							p+=9;
						}
						p-=8;
						while(*p){
							p-=9;
						}
					}
					p+=9;
					while(*p){
						p+=9;
					}
					p-=9;
					while(*p){
						p++;
						while(*p){
							(*p)--;
							(*(p+9))++;
						}
						p-=10;
					}
					p++;
					while(*p){
						(*p)--;
						(*(p+9))++;
					}
					(*(p-1))++;
					p+=7;
				}
				p-=9;
				while(*p){
					p++;
					(*p)=0;
					(*(p-1))--;
					p+=2;
					while(*p){
						(*p)--;
						(*(p-3))++;
						p-=2;
						while(*p){
							(*(p-1))--;
							(*p)--;
							(*(p-7))++;
						}
						p--;
						while(*p){
							(*p)--;
							(*(p+1))++;
						}
						p+=3;
					}
					p-=2;
					while(*p){
						(*p)--;
						(*(p+2))++;
					}
					(*(p-1))++;
					p-=10;
				}
				p+=9;
				while(*p){
					p+=6;
					while(*p){
						(*p)--;
						(*(p-5))++;
					}
					p-=5;
					while(*p){
						(*p)--;
						(*(p+5))++;
						(*(p+1))++;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					(*(p+1))++;
					p+=9;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					(*(p+1))--;
					p+=6;
					while(*p){
						(*p)--;
						(*(p-5))++;
					}
					p-=5;
					while(*p){
						(*p)--;
						(*(p+5))++;
						p--;
						while(*p){
							(*p)--;
							p+=2;
							while(*p){
								(*p)--;
								(*(p-2))++;
							}
							p-=2;
							while(*p){
								(*p)--;
								(*(p+2))++;
								(*(p+4))++;
							}
							(*p)++;
							p+=9;
						}
						p-=8;
						while(*p){
							p-=9;
						}
					}
					p+=9;
					while(*p){
						p+=9;
					}
					p-=9;
					while(*p){
						p++;
						while(*p){
							(*p)--;
							(*(p+9))++;
						}
						p-=10;
					}
					p++;
					while(*p){
						(*p)--;
						(*(p+9))++;
					}
					(*(p-1))++;
					p+=7;
				}
				p-=9;
				while(*p){
					p++;
					(*p)=0;
					(*(p-1))--;
					p+=3;
					while(*p){
						(*p)--;
						(*(p-4))++;
						p-=3;
						while(*p){
							(*(p-1))--;
							(*p)--;
							(*(p-6))++;
						}
						p--;
						while(*p){
							(*p)--;
							(*(p+1))++;
						}
						p+=4;
					}
					p-=3;
					while(*p){
						(*p)--;
						(*(p+3))++;
					}
					(*(p-1))++;
					p-=10;
				}
				p+=9;
				while(*p){
					p+=4;
					while(*p){
						(*p)--;
						(*(p-36))++;
					}
					p+=5;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					p+=3;
					while(*p){
						(*p)--;
						(*(p-36))++;
					}
					p+=6;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				(*p)+=15;
				while(*p){
					while(*p){
						p+=9;
					}
					(*(p-9))--;
					p-=18;
					while(*p){
						p-=9;
					}
					p+=9;
					(*p)--;
				}
				(*p)++;
				while(*p){
					p+=8;
					while(*p){
						(*p)--;
						(*(p-7))++;
					}
					p-=7;
					while(*p){
						(*p)--;
						(*(p+7))++;
						(*(p+1))++;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					p+=6;
					(*p)=0;
					p+=3;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				(*(p+4))++;
				p+=5;
				while(*p){
					(*p)--;
					(*(p-1))--;
					(*(p-5))++;
				}
				p++;
				while(*p){
					(*p)--;
					p-=6;
					while(*p){
						(*p)--;
						(*(p+5))++;
						(*(p+4))+=2;
					}
					p+=5;
					while(*p){
						(*p)--;
						(*(p-5))++;
					}
					(*(p-1))--;
					(*p)++;
					p++;
				}
				p--;
				while(*p){
					(*p)--;
					(*(p+1))++;
				}
				p-=5;
				while(*p){
					(*p)--;
					(*(p+5))++;
				}
				p+=6;
				(*p)=0;
				(*(p-6))++;
				p-=2;
				while(*p){
					(*p)--;
					(*(p-4))--;
				}
				(*p)++;
				p-=4;
				while(*p){
					(*p)--;
					(*(p+4))--;
					p+=9;
					while(*p){
						p+=2;
						while(*p){
							(*p)--;
							(*(p-2))--;
						}
						(*p)++;
						p-=2;
						while(*p){
							(*p)--;
							(*(p+2))--;
							p+=3;
							while(*p){
								(*p)--;
								(*(p-3))++;
							}
							p-=3;
							while(*p){
								(*p)--;
								(*(p+3))++;
								p-=9;
								while(*p){
									p-=9;
								}
								(*(p+3))=1;
								p+=9;
								while(*p){
									p+=9;
								}
								(*(p+1))++;
							}
						}
						(*p)++;
						p+=3;
						while(*p){
							(*p)--;
							(*(p-3))--;
						}
						(*p)++;
						p-=3;
						while(*p){
							(*p)--;
							(*(p+3))--;
							p+=2;
							while(*p){
								(*p)--;
								(*(p-2))++;
							}
							p-=2;
							while(*p){
								(*p)--;
								(*(p+2))++;
								p-=9;
								while(*p){
									p-=9;
								}
								(*(p+4))=1;
								p+=9;
								while(*p){
									p+=9;
								}
								(*(p+1))=1;
							}
						}
						(*p)++;
						p++;
						while(*p){
							(*p)--;
							p--;
							while(*p){
								p+=9;
							}
							p-=8;
						}
						p+=8;
					}
					p-=9;
					while(*p){
						p-=9;
					}
					p+=4;
					while(*p){
						(*p)--;
						(*(p-4))++;
					}
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))++;
						p+=9;
						while(*p){
							(*(p+1))++;
							p+=3;
							while(*p){
								(*p)--;
								(*(p-2))--;
							}
							p-=2;
							while(*p){
								(*p)--;
								(*(p+2))++;
							}
							p+=8;
						}
						(*(p-8))++;
						p-=9;
						while(*p){
							p++;
							while(*p){
								(*p)--;
								(*(p+5))++;
								p++;
								while(*p){
									(*p)--;
									(*(p+4))--;
									(*(p-10))++;
									p++;
									while(*p){
										(*p)--;
										(*(p+3))++;
									}
									p--;
								}
								p++;
								while(*p){
									(*p)--;
									(*(p+3))--;
									(*(p-11))++;
								}
								p-=2;
							}
							p++;
							while(*p){
								(*p)--;
								(*(p+4))++;
								p++;
								while(*p){
									(*p)--;
									(*(p+3))--;
									(*(p-11))++;
								}
								p--;
							}
							p++;
							while(*p){
								(*p)--;
								(*(p+3))++;
							}
							p-=12;
						}
						p+=4;
						(*p)=0;
						p-=4;
					}
					p+=3;
					while(*p){
						(*p)--;
						(*(p-3))++;
					}
					p-=3;
					while(*p){
						(*p)--;
						(*(p+3))++;
						p+=9;
						while(*p){
							(*(p+1))++;
							p+=2;
							while(*p){
								(*p)--;
								(*(p-1))--;
							}
							p--;
							while(*p){
								(*p)--;
								(*(p+1))++;
							}
							p+=8;
						}
						(*(p-8))++;
						p-=9;
						while(*p){
							p++;
							while(*p){
								(*p)--;
								(*(p+5))++;
								p+=2;
								while(*p){
									(*p)--;
									(*(p+3))--;
									(*(p-11))++;
									p--;
									while(*p){
										(*p)--;
										(*(p+4))++;
									}
									p++;
								}
								p--;
								while(*p){
									(*p)--;
									(*(p+4))--;
									(*(p-10))++;
								}
								p--;
							}
							p+=2;
							while(*p){
								(*p)--;
								(*(p+3))++;
								p--;
								while(*p){
									(*p)--;
									(*(p+4))--;
									(*(p-10))++;
								}
								p++;
							}
							p--;
							while(*p){
								(*p)--;
								(*(p+4))++;
							}
							p-=11;
						}
						(*(p+6))++;
					}
				}
				p+=4;
				while(*p){
					(*p)--;
					(*(p-4))++;
				}
				p-=4;
				while(*p){
					(*p)--;
					(*(p+4))++;
					p+=9;
					while(*p){
						p+=9;
					}
					p-=9;
					while(*p){
						p++;
						while(*p){
							(*p)--;
							(*(p+5))++;
							p++;
							while(*p){
								(*p)--;
								(*(p+4))--;
								(*(p-10))++;
								p++;
								while(*p){
									(*p)--;
									(*(p+3))++;
								}
								p--;
							}
							p++;
							while(*p){
								(*p)--;
								(*(p+3))--;
								(*(p-11))++;
							}
							p-=2;
						}
						p++;
						while(*p){
							(*p)--;
							(*(p+4))++;
							p++;
							while(*p){
								(*p)--;
								(*(p+3))--;
								(*(p-11))++;
							}
							p--;
						}
						p++;
						while(*p){
							(*p)--;
							(*(p+3))++;
						}
						p-=12;
					}
				}
				p++;
				(*p)=0;
				p+=2;
				(*p)=0;
				p++;
				(*p)=0;
				p+=5;
				while(*p){
					p+=2;
					(*p)=0;
					p++;
					(*p)=0;
					p+=6;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					p+=5;
					while(*p){
						(*p)--;
						(*(p-4))++;
					}
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))++;
						(*(p+1))++;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				(*p)+=15;
				while(*p){
					while(*p){
						p+=9;
					}
					(*p)++;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p-=9;
					while(*p){
						p-=9;
					}
					p+=9;
					(*p)--;
				}
				(*p)++;
				while(*p){
					(*(p+1))++;
					p+=9;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					(*(p+1))--;
					p+=5;
					while(*p){
						(*p)--;
						(*(p-4))++;
					}
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))++;
						p--;
						while(*p){
							(*p)--;
							p+=2;
							while(*p){
								(*p)--;
								(*(p-2))++;
							}
							p-=2;
							while(*p){
								(*p)--;
								(*(p+2))++;
								(*(p+3))++;
							}
							(*p)++;
							p+=9;
						}
						p-=8;
						while(*p){
							p-=9;
						}
					}
					p+=9;
					while(*p){
						p+=9;
					}
					p-=9;
					while(*p){
						p++;
						while(*p){
							(*p)--;
							(*(p+9))++;
						}
						p-=10;
					}
					p++;
					while(*p){
						(*p)--;
						(*(p+9))++;
					}
					(*(p-1))++;
					p+=7;
				}
				p-=9;
				while(*p){
					p++;
					(*p)=0;
					(*(p-1))--;
					p+=2;
					while(*p){
						(*p)--;
						(*(p-3))++;
						p-=2;
						while(*p){
							(*(p-1))--;
							(*p)--;
							(*(p-7))++;
						}
						p--;
						while(*p){
							(*p)--;
							(*(p+1))++;
						}
						p+=3;
					}
					p-=2;
					while(*p){
						(*p)--;
						(*(p+2))++;
					}
					(*(p-1))++;
					p-=10;
				}
				p+=9;
				while(*p){
					p+=3;
					while(*p){
						(*p)--;
						(*(p-36))++;
					}
					p+=6;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=5;
				(*p)=0;
				p+=4;
				(*p)+=15;
				while(*p){
					while(*p){
						p+=9;
					}
					(*(p-9))--;
					p-=18;
					while(*p){
						p-=9;
					}
					p+=9;
					(*p)--;
				}
				(*p)++;
				while(*p){
					p+=3;
					while(*p){
						(*p)--;
						(*(p-3))--;
					}
					(*p)++;
					p-=3;
					while(*p){
						(*p)--;
						(*(p+3))--;
						p+=4;
						while(*p){
							(*p)--;
							(*(p-4))++;
						}
						p-=4;
						while(*p){
							(*p)--;
							(*(p+4))++;
							p-=9;
							while(*p){
								p-=9;
							}
							(*(p+4))=1;
							p+=9;
							while(*p){
								p+=9;
							}
							(*(p+1))++;
						}
					}
					(*p)++;
					p+=4;
					while(*p){
						(*p)--;
						(*(p-4))--;
					}
					(*p)++;
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))--;
						p+=3;
						while(*p){
							(*p)--;
							(*(p-3))++;
						}
						p-=3;
						while(*p){
							(*p)--;
							(*(p+3))++;
							p-=9;
							while(*p){
								p-=9;
							}
							(*(p+3))=1;
							p+=9;
							while(*p){
								p+=9;
							}
							(*(p+1))=1;
						}
					}
					(*p)++;
					p++;
					while(*p){
						(*p)--;
						p--;
						while(*p){
							p+=9;
						}
						p-=8;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=3;
				while(*p){
					(*p)--;
					(*(p-3))++;
				}
				p-=3;
				while(*p){
					(*p)--;
					(*(p+3))++;
					p+=9;
					while(*p){
						(*(p+1))++;
						p+=4;
						while(*p){
							(*p)--;
							(*(p-3))--;
						}
						p-=3;
						while(*p){
							(*p)--;
							(*(p+3))++;
						}
						p+=8;
					}
					(*(p-8))++;
					p-=9;
					while(*p){
						p++;
						while(*p){
							(*p)--;
							(*(p+1))++;
							p+=2;
							while(*p){
								(*p)--;
								(*(p-1))--;
								(*(p-11))++;
								p++;
								while(*p){
									(*p)--;
									(*(p-2))++;
								}
								p--;
							}
							p++;
							while(*p){
								(*p)--;
								(*(p-2))--;
								(*(p-12))++;
							}
							p-=3;
						}
						p+=2;
						while(*p){
							(*p)--;
							(*(p-1))++;
							p++;
							while(*p){
								(*p)--;
								(*(p-2))--;
								(*(p-12))++;
							}
							p--;
						}
						p++;
						while(*p){
							(*p)--;
							(*(p-2))++;
						}
						p-=13;
					}
				}
				p+=4;
				while(*p){
					(*p)--;
					(*(p-4))++;
				}
				p-=4;
				while(*p){
					(*p)--;
					(*(p+4))++;
					p+=9;
					while(*p){
						(*(p+1))++;
						p+=3;
						while(*p){
							(*p)--;
							(*(p-2))--;
						}
						p-=2;
						while(*p){
							(*p)--;
							(*(p+2))++;
						}
						p+=8;
					}
					(*(p-8))++;
					p-=9;
					while(*p){
						p++;
						while(*p){
							(*p)--;
							(*(p+1))++;
							p+=3;
							while(*p){
								(*p)--;
								(*(p-2))--;
								(*(p-12))++;
								p--;
								while(*p){
									(*p)--;
									(*(p-1))++;
								}
								p++;
							}
							p--;
							while(*p){
								(*p)--;
								(*(p-1))--;
								(*(p-11))++;
							}
							p-=2;
						}
						p+=3;
						while(*p){
							(*p)--;
							(*(p-2))++;
							p--;
							while(*p){
								(*p)--;
								(*(p-1))--;
								(*(p-11))++;
							}
							p++;
						}
						p--;
						while(*p){
							(*p)--;
							(*(p-1))++;
						}
						p-=12;
					}
					(*(p+5))++;
				}
				p+=9;
				while(*p){
					p+=3;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p+=4;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=3;
				(*p)=0;
				p++;
				(*p)=0;
				p+=5;
				while(*p){
					p+=7;
					while(*p){
						(*p)--;
						(*(p-6))++;
					}
					p-=6;
					while(*p){
						(*p)--;
						(*(p+6))++;
						(*(p+2))++;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				(*(p+4))++;
				p+=5;
				while(*p){
					(*p)--;
					(*(p-1))--;
					(*(p-5))++;
				}
				p+=2;
				while(*p){
					(*p)--;
					p-=7;
					while(*p){
						(*p)--;
						(*(p+5))++;
						(*(p+4))+=2;
					}
					p+=5;
					while(*p){
						(*p)--;
						(*(p-5))++;
					}
					(*(p-1))--;
					(*p)++;
					p+=2;
				}
				p-=2;
				while(*p){
					(*p)--;
					(*(p+2))++;
				}
				p-=5;
				while(*p){
					(*p)--;
					(*(p+5))++;
				}
				(*p)++;
				p+=4;
				while(*p){
					(*p)--;
					(*(p-4))--;
				}
				(*p)++;
				p-=4;
				while(*p){
					(*p)--;
					(*(p+4))--;
					p+=9;
					while(*p){
						p+=3;
						while(*p){
							(*p)--;
							(*(p-3))--;
						}
						(*p)++;
						p-=3;
						while(*p){
							(*p)--;
							(*(p+3))--;
							p+=2;
							while(*p){
								(*p)--;
								(*(p-2))++;
							}
							p-=2;
							while(*p){
								(*p)--;
								(*(p+2))++;
								p-=9;
								while(*p){
									p-=9;
								}
								(*(p+4))=1;
								p+=9;
								while(*p){
									p+=9;
								}
								(*(p+1))++;
							}
						}
						(*p)++;
						p+=2;
						while(*p){
							(*p)--;
							(*(p-2))--;
						}
						(*p)++;
						p-=2;
						while(*p){
							(*p)--;
							(*(p+2))--;
							p+=3;
							while(*p){
								(*p)--;
								(*(p-3))++;
							}
							p-=3;
							while(*p){
								(*p)--;
								(*(p+3))++;
								p-=9;
								while(*p){
									p-=9;
								}
								(*(p+3))=1;
								p+=9;
								while(*p){
									p+=9;
								}
								(*(p+1))=1;
							}
						}
						(*p)++;
						p++;
						while(*p){
							(*p)--;
							p--;
							while(*p){
								p+=9;
							}
							p-=8;
						}
						p+=8;
					}
					p-=9;
					while(*p){
						p-=9;
					}
					p+=3;
					while(*p){
						(*p)--;
						(*(p-3))++;
					}
					p-=3;
					while(*p){
						(*p)--;
						(*(p+3))++;
						p+=9;
						while(*p){
							(*(p+1))++;
							p+=2;
							while(*p){
								(*p)--;
								(*(p-1))--;
							}
							p--;
							while(*p){
								(*p)--;
								(*(p+1))++;
							}
							p+=8;
						}
						(*(p-8))++;
						p-=9;
						while(*p){
							p++;
							while(*p){
								(*p)--;
								(*(p+4))++;
								p+=2;
								while(*p){
									(*p)--;
									(*(p+2))--;
									(*(p-11))++;
									p--;
									while(*p){
										(*p)--;
										(*(p+3))++;
									}
									p++;
								}
								p--;
								while(*p){
									(*p)--;
									(*(p+3))--;
									(*(p-10))++;
								}
								p--;
							}
							p+=2;
							while(*p){
								(*p)--;
								(*(p+2))++;
								p--;
								while(*p){
									(*p)--;
									(*(p+3))--;
									(*(p-10))++;
								}
								p++;
							}
							p--;
							while(*p){
								(*p)--;
								(*(p+3))++;
							}
							p-=11;
						}
						p+=5;
						(*p)=0;
						p+=2;
						while(*p){
							(*p)--;
							(*(p-7))++;
						}
						p-=7;
						while(*p){
							(*p)--;
							(*(p+7))++;
							(*(p+5))++;
						}
					}
					p+=4;
					while(*p){
						(*p)--;
						(*(p-4))++;
					}
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))++;
						p+=9;
						while(*p){
							(*(p+1))++;
							p+=3;
							while(*p){
								(*p)--;
								(*(p-2))--;
							}
							p-=2;
							while(*p){
								(*p)--;
								(*(p+2))++;
							}
							p+=8;
						}
						(*(p-8))++;
						p-=9;
						while(*p){
							p++;
							while(*p){
								(*p)--;
								(*(p+4))++;
								p++;
								while(*p){
									(*p)--;
									(*(p+3))--;
									(*(p-10))++;
									p++;
									while(*p){
										(*p)--;
										(*(p+2))++;
									}
									p--;
								}
								p++;
								while(*p){
									(*p)--;
									(*(p+2))--;
									(*(p-11))++;
								}
								p-=2;
							}
							p++;
							while(*p){
								(*p)--;
								(*(p+3))++;
								p++;
								while(*p){
									(*p)--;
									(*(p+2))--;
									(*(p-11))++;
								}
								p--;
							}
							p++;
							while(*p){
								(*p)--;
								(*(p+2))++;
							}
							p-=12;
						}
					}
					p+=4;
					(*p)=0;
					p-=4;
				}
				p+=4;
				while(*p){
					(*p)--;
					(*(p-4))++;
				}
				p-=4;
				while(*p){
					(*p)--;
					(*(p+4))++;
					p+=5;
					(*p)=0;
					p+=2;
					while(*p){
						(*p)--;
						(*(p-7))++;
					}
					p-=7;
					while(*p){
						(*p)--;
						(*(p+7))++;
						(*(p+5))++;
					}
					p+=9;
					while(*p){
						p+=9;
					}
					p-=9;
					while(*p){
						p++;
						while(*p){
							(*p)--;
							(*(p+4))++;
							p++;
							while(*p){
								(*p)--;
								(*(p+3))--;
								(*(p-10))++;
								p++;
								while(*p){
									(*p)--;
									(*(p+2))++;
								}
								p--;
							}
							p++;
							while(*p){
								(*p)--;
								(*(p+2))--;
								(*(p-11))++;
							}
							p-=2;
						}
						p++;
						while(*p){
							(*p)--;
							(*(p+3))++;
							p++;
							while(*p){
								(*p)--;
								(*(p+2))--;
								(*(p-11))++;
							}
							p--;
						}
						p++;
						while(*p){
							(*p)--;
							(*(p+2))++;
						}
						p-=12;
					}
				}
				p+=9;
				while(*p){
					p+=2;
					(*p)=0;
					p++;
					(*p)=0;
					p+=6;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=3;
				(*p)=0;
				p++;
				(*p)=0;
				p+=5;
				while(*p){
					p+=5;
					while(*p){
						(*p)--;
						(*(p-4))++;
					}
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))++;
						(*(p+1))++;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					p+=6;
					while(*p){
						(*p)--;
						(*(p-5))++;
					}
					p-=5;
					while(*p){
						(*p)--;
						(*(p+5))++;
						(*(p+2))++;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				(*p)+=15;
				while(*p){
					while(*p){
						p+=9;
					}
					(*p)++;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p++;
					(*p)=0;
					p-=9;
					while(*p){
						p-=9;
					}
					p+=9;
					(*p)--;
				}
				(*p)++;
				while(*p){
					(*(p+1))++;
					p+=9;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					(*(p+1))--;
					p+=5;
					while(*p){
						(*p)--;
						(*(p-4))++;
					}
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))++;
						p--;
						while(*p){
							(*p)--;
							p+=2;
							while(*p){
								(*p)--;
								(*(p-2))++;
							}
							p-=2;
							while(*p){
								(*p)--;
								(*(p+2))++;
								(*(p+4))++;
							}
							(*p)++;
							p+=9;
						}
						p-=8;
						while(*p){
							p-=9;
						}
					}
					p+=9;
					while(*p){
						p+=9;
					}
					p-=9;
					while(*p){
						p++;
						while(*p){
							(*p)--;
							(*(p+9))++;
						}
						p-=10;
					}
					p++;
					while(*p){
						(*p)--;
						(*(p+9))++;
					}
					(*(p-1))++;
					p+=7;
				}
				p-=9;
				while(*p){
					p++;
					(*p)=0;
					(*(p-1))--;
					p+=3;
					while(*p){
						(*p)--;
						(*(p-4))++;
						p-=3;
						while(*p){
							(*(p-1))--;
							(*p)--;
							(*(p-6))++;
						}
						p--;
						while(*p){
							(*p)--;
							(*(p+1))++;
						}
						p+=4;
					}
					p-=3;
					while(*p){
						(*p)--;
						(*(p+3))++;
					}
					(*(p-1))++;
					p-=10;
				}
				p+=9;
				while(*p){
					(*(p+1))++;
					p+=9;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					(*(p+1))--;
					p+=6;
					while(*p){
						(*p)--;
						(*(p-5))++;
					}
					p-=5;
					while(*p){
						(*p)--;
						(*(p+5))++;
						p--;
						while(*p){
							(*p)--;
							p+=3;
							while(*p){
								(*p)--;
								(*(p-3))++;
							}
							p-=3;
							while(*p){
								(*p)--;
								(*(p+3))++;
								(*(p+4))++;
							}
							(*p)++;
							p+=9;
						}
						p-=8;
						while(*p){
							p-=9;
						}
					}
					p+=9;
					while(*p){
						p+=9;
					}
					p-=9;
					while(*p){
						p+=2;
						while(*p){
							(*p)--;
							(*(p+9))++;
						}
						p-=11;
					}
					p+=2;
					while(*p){
						(*p)--;
						(*(p+9))++;
					}
					(*(p-2))++;
					p+=6;
				}
				p-=9;
				while(*p){
					p++;
					(*p)=0;
					(*(p-1))--;
					p+=3;
					while(*p){
						(*p)--;
						(*(p-4))++;
						p-=3;
						while(*p){
							(*(p-1))--;
							(*p)--;
							(*(p-6))++;
						}
						p--;
						while(*p){
							(*p)--;
							(*(p+1))++;
						}
						p+=4;
					}
					p-=3;
					while(*p){
						(*p)--;
						(*(p+3))++;
					}
					(*(p-1))++;
					p-=10;
				}
				p+=9;
				while(*p){
					p+=4;
					while(*p){
						(*p)--;
						(*(p-36))++;
					}
					p+=5;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=9;
				(*p)+=15;
				while(*p){
					while(*p){
						p+=9;
					}
					(*(p-9))--;
					p-=18;
					while(*p){
						p-=9;
					}
					p+=9;
					(*p)--;
				}
				(*p)++;
				(*(p+21))++;
				p+=18;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					p+=3;
					while(*p){
						(*p)--;
						(*(p-3))--;
					}
					(*p)++;
					p-=3;
					while(*p){
						(*p)--;
						(*(p+3))--;
						p+=4;
						while(*p){
							(*p)--;
							(*(p-4))++;
						}
						p-=4;
						while(*p){
							(*p)--;
							(*(p+4))++;
							p-=9;
							while(*p){
								p-=9;
							}
							(*(p+4))=1;
							p+=9;
							while(*p){
								p+=9;
							}
							(*(p+1))++;
						}
					}
					(*p)++;
					p+=4;
					while(*p){
						(*p)--;
						(*(p-4))--;
					}
					(*p)++;
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))--;
						p+=3;
						while(*p){
							(*p)--;
							(*(p-3))++;
						}
						p-=3;
						while(*p){
							(*p)--;
							(*(p+3))++;
							p-=9;
							while(*p){
								p-=9;
							}
							(*(p+3))=1;
							p+=9;
							while(*p){
								p+=9;
							}
							(*(p+1))=1;
						}
					}
					(*p)++;
					p++;
					while(*p){
						(*p)--;
						p--;
						while(*p){
							p+=9;
						}
						p-=8;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				(*(p+2))--;
				p+=4;
				while(*p){
					(*p)--;
					(*(p-4))++;
				}
				p-=4;
				while(*p){
					(*p)--;
					(*(p+4))++;
					p+=2;
					(*p)=0;
					p-=2;
				}
				p+=2;
			}
			(*(p-2))++;
			p+=2;
			while(*p){
				(*p)--;
				(*(p-4))--;
			}
			(*p)++;
			p-=4;
			while(*p){
				(*p)--;
				(*(p+4))--;
				p-=2;
				putchar((*p));
				p+=2;
			}
			p+=4;
			while(*p){
				(*p)--;
				p-=7;
				putchar((*p));
				p+=7;
			}
			p-=3;
			(*p)=0;
			p++;
			(*p)=0;
			p++;
			(*p)=0;
			p++;
			(*p)=0;
			p++;
			(*p)=0;
			p++;
			(*p)=0;
			p+=3;
			while(*p){
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p++;
				(*p)=0;
				p+=3;
			}
			p-=9;
			while(*p){
				p-=9;
			}
			p+=9;
			while(*p){
				p+=5;
				(*p)=0;
				p+=4;
			}
			p-=9;
			while(*p){
				p-=9;
			}
			p++;
			(*p)+=11;
			while(*p){
				(*p)--;
				while(*p){
					(*p)--;
					(*(p+9))++;
				}
				p+=9;
			}
			(*(p+4))++;
			(*(p+13))++;
			p--;
			while(*p){
				p-=9;
			}
			p+=7;
			while(*p){
				(*p)--;
				(*(p-7))++;
			}
			p-=7;
			while(*p){
				(*p)--;
				p+=7;
				(*p)++;
				(*p)=0;
				p+=2;
				while(*p){
					p+=9;
				}
				p-=9;
				while(*p){
					p+=7;
					while(*p){
						(*p)--;
						(*(p-6))++;
					}
					p-=6;
					while(*p){
						(*p)--;
						(*(p+6))++;
						p--;
						while(*p){
							p-=9;
						}
						(*(p+7))=1;
						p+=10;
					}
					p-=10;
				}
			}
			p+=7;
			while(*p){
				(*p)--;
				(*(p-7))++;
			}
			p-=7;
			while(*p){
				(*p)--;
				(*(p+7))++;
				p+=9;
				while(*p){
					(*(p+1))++;
					p+=5;
					while(*p){
						(*p)--;
						(*(p-4))--;
					}
					p-=4;
					while(*p){
						(*p)--;
						(*(p+4))++;
					}
					p+=8;
				}
				(*(p-2))++;
				p-=9;
				while(*p){
					p+=5;
					while(*p){
						(*p)--;
						(*(p+2))++;
					}
					p-=14;
				}
				p+=9;
				while(*p){
					p+=9;
				}
				p-=9;
				while(*p){
					p++;
					(*p)=0;
					(*(p-1))--;
					p+=6;
					while(*p){
						(*p)--;
						(*(p-7))++;
						p-=6;
						while(*p){
							(*(p-1))--;
							(*p)--;
							(*(p-3))++;
						}
						p--;
						while(*p){
							(*p)--;
							(*(p+1))++;
						}
						p+=7;
					}
					p-=6;
					while(*p){
						(*p)--;
						(*(p+6))++;
					}
					(*(p-1))++;
					p-=10;
				}
				(*(p+7))--;
				(*(p+3))=1;
			}
			(*p)++;
			p+=7;
			while(*p){
				(*p)--;
				(*(p-7))--;
			}
			(*p)++;
			p-=7;
			while(*p){
				(*p)--;
				(*(p+7))--;
				p+=9;
				while(*p){
					p+=5;
					while(*p){
						(*p)--;
						(*(p+2))++;
					}
					p+=4;
				}
				p-=9;
				while(*p){
					p++;
					(*p)=0;
					(*(p-1))--;
					p+=6;
					while(*p){
						(*p)--;
						(*(p-7))++;
						p-=6;
						while(*p){
							(*(p-1))--;
							(*p)--;
							(*(p-3))++;
						}
						p--;
						while(*p){
							(*p)--;
							(*(p+1))++;
						}
						p+=7;
					}
					p-=6;
					while(*p){
						(*p)--;
						(*(p+6))++;
					}
					(*(p-1))++;
					p-=10;
				}
				p++;
				(*p)+=5;
				while(*p){
					(*p)--;
					while(*p){
						(*p)--;
						(*(p+9))++;
					}
					p+=9;
				}
				(*(p+4))++;
				p--;
				while(*p){
					p-=9;
				}
				p+=9;
				while(*p){
					p+=5;
					while(*p){
						(*p)--;
						(*(p-5))--;
					}
					(*p)++;
					p-=5;
					while(*p){
						(*p)--;
						(*(p+5))--;
						p+=7;
						while(*p){
							(*p)--;
							(*(p-7))++;
						}
						p-=7;
						while(*p){
							(*p)--;
							(*(p+7))++;
							p-=9;
							while(*p){
								p-=9;
							}
							(*(p+4))=1;
							p+=9;
							while(*p){
								p+=9;
							}
							(*(p+1))++;
						}
					}
					(*p)++;
					p+=7;
					while(*p){
						(*p)--;
						(*(p-7))--;
					}
					(*p)++;
					p-=7;
					while(*p){
						(*p)--;
						(*(p+7))--;
						p+=5;
						while(*p){
							(*p)--;
							(*(p-5))++;
						}
						p-=5;
						while(*p){
							(*p)--;
							(*(p+5))++;
							p-=9;
							while(*p){
								p-=9;
							}
							(*(p+3))=1;
							p+=9;
							while(*p){
								p+=9;
							}
							(*(p+1))=1;
						}
					}
					(*p)++;
					p++;
					while(*p){
						(*p)--;
						p--;
						while(*p){
							p+=9;
						}
						p-=8;
					}
					p+=8;
				}
				p-=9;
				while(*p){
					p-=9;
				}
				p+=4;
				(*p)=0;
				p-=3;
				(*p)+=5;
				while(*p){
					(*p)--;
					while(*p){
						(*p)--;
						(*(p+9))++;
					}
					p+=9;
				}
				(*(p+4))--;
				p--;
				while(*p){
					p-=9;
				}
			}
			p+=3;
		}
		p-=4;
		putchar((*p));
		p+=10;
		while(*p){
			p+=6;
			(*p)=0;
			p+=3;
		}
		p-=9;
		while(*p){
			p-=9;
		}
		p++;
		(*p)+=10;
		while(*p){
			(*p)--;
			while(*p){
				(*p)--;
				(*(p+9))++;
			}
			p+=9;
		}
		(*(p+5))++;
		(*(p+14))++;
		p--;
		while(*p){
			p-=9;
		}
		p+=8;
		while(*p){
			(*p)--;
			(*(p-8))++;
		}
		p-=8;
		while(*p){
			(*p)--;
			p+=8;
			(*p)++;
			(*p)=0;
			p++;
			while(*p){
				p+=9;
			}
			p-=9;
			while(*p){
				p+=8;
				while(*p){
					(*p)--;
					(*(p-7))++;
				}
				p-=7;
				while(*p){
					(*p)--;
					(*(p+7))++;
					p--;
					while(*p){
						p-=9;
					}
					(*(p+8))=1;
					p+=10;
				}
				p-=10;
			}
		}
		p+=8;
		while(*p){
			(*p)--;
			(*(p-8))++;
		}
		p-=8;
		while(*p){
			(*p)--;
			(*(p+8))++;
			p+=9;
			while(*p){
				(*(p+1))++;
				p+=6;
				while(*p){
					(*p)--;
					(*(p-5))--;
				}
				p-=5;
				while(*p){
					(*p)--;
					(*(p+5))++;
				}
				p+=8;
			}
			(*(p-1))++;
			p-=9;
			while(*p){
				p+=6;
				while(*p){
					(*p)--;
					(*(p+2))++;
				}
				p-=15;
			}
			p+=9;
			while(*p){
				p+=9;
			}
			p-=9;
			while(*p){
				p++;
				(*p)=0;
				(*(p-1))--;
				p+=7;
				while(*p){
					(*p)--;
					(*(p-8))++;
					p-=7;
					while(*p){
						(*(p-1))--;
						(*p)--;
						(*(p-2))++;
					}
					p--;
					while(*p){
						(*p)--;
						(*(p+1))++;
					}
					p+=8;
				}
				p-=7;
				while(*p){
					(*p)--;
					(*(p+7))++;
				}
				(*(p-1))++;
				p-=10;
			}
			(*(p+8))--;
			(*(p+3))=1;
		}
		(*p)++;
		p+=8;
		while(*p){
			(*p)--;
			(*(p-8))--;
		}
		(*p)++;
		p-=8;
		while(*p){
			(*p)--;
			(*(p+8))--;
			p+=9;
			while(*p){
				p+=6;
				while(*p){
					(*p)--;
					(*(p+2))++;
				}
				p+=3;
			}
			p-=9;
			while(*p){
				p++;
				(*p)=0;
				(*(p-1))--;
				p+=7;
				while(*p){
					(*p)--;
					(*(p-8))++;
					p-=7;
					while(*p){
						(*(p-1))--;
						(*p)--;
						(*(p-2))++;
					}
					p--;
					while(*p){
						(*p)--;
						(*(p+1))++;
					}
					p+=8;
				}
				p-=7;
				while(*p){
					(*p)--;
					(*(p+7))++;
				}
				(*(p-1))++;
				p-=10;
			}
			p++;
			(*p)+=5;
			while(*p){
				(*p)--;
				while(*p){
					(*p)--;
					(*(p+9))++;
				}
				p+=9;
			}
			(*(p+5))++;
			(*(p+32))++;
			p+=26;
			while(*p){
				p-=9;
			}
			p+=9;
			while(*p){
				p+=6;
				while(*p){
					(*p)--;
					(*(p-6))--;
				}
				(*p)++;
				p-=6;
				while(*p){
					(*p)--;
					(*(p+6))--;
					p+=8;
					while(*p){
						(*p)--;
						(*(p-8))++;
					}
					p-=8;
					while(*p){
						(*p)--;
						(*(p+8))++;
						p-=9;
						while(*p){
							p-=9;
						}
						(*(p+4))=1;
						p+=9;
						while(*p){
							p+=9;
						}
						(*(p+1))++;
					}
				}
				(*p)++;
				p+=8;
				while(*p){
					(*p)--;
					(*(p-8))--;
				}
				(*p)++;
				p-=8;
				while(*p){
					(*p)--;
					(*(p+8))--;
					p+=6;
					while(*p){
						(*p)--;
						(*(p-6))++;
					}
					p-=6;
					while(*p){
						(*p)--;
						(*(p+6))++;
						p-=9;
						while(*p){
							p-=9;
						}
						(*(p+3))=1;
						p+=9;
						while(*p){
							p+=9;
						}
						(*(p+1))=1;
					}
				}
				(*p)++;
				p++;
				while(*p){
					(*p)--;
					p--;
					while(*p){
						p+=9;
					}
					p-=8;
				}
				p+=8;
			}
			p-=9;
			while(*p){
				p-=9;
			}
			p+=4;
			(*p)=0;
			p-=3;
			(*p)+=5;
			while(*p){
				(*p)--;
				while(*p){
					(*p)--;
					(*(p+9))++;
				}
				p+=9;
			}
			(*(p+5))--;
			(*(p+32))--;
			p+=26;
			while(*p){
				p-=9;
			}
		}
		p+=3;
	}
}