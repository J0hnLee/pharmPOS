import * as actionTypes from '../constants';
const userInfo = (state = {}, action) => {
	switch (action.type) {
		case actionTypes.SET_USERINFO:
			return action.data;
		default:
			return state;
	}
};

export default userInfo;
